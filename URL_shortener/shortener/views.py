from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Url
import random
import string

@api_view(['POST'])
def create_shortened_url(request):
    original_url = request.data.get('original_url')
    if not original_url:
        return Response({'error': 'Original URL is required'}, status=status.HTTP_400_BAD_REQUEST)

    shortened_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    url = Url.objects.create(original_url=original_url, short_code=shortened_url)
    return Response({'shortened_url': f'http://localhost:8000/{shortened_url}'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def redirect_to_original_url(request, short_code):
    try:
        url = Url.objects.get(short_code=short_code)
        return Response({'original_url': url.original_url}, status=status.HTTP_302_FOUND)
    except Url.DoesNotExist:
        return Response({'error': 'Shortened URL not found.'}, status=status.HTTP_404_NOT_FOUND)

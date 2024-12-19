from django.shortcuts import render
from django.http import JsonResponse
from shortener.models import Url
from django.utils.crypto import get_random_string
from django.shortcuts import redirect


def create_shortened_url(request):
    if request.method == 'POST':
        original_url = request.POST.get('original_url')

        if original_url:
            short_code = get_random_string(6)

            shortened_url = Url.objects.create(
                original_url=original_url,
                short_code=short_code
            )

            return JsonResponse({'shortened_url': f'http://localhost:8000/{short_code}'})

    return render(request, 'create_url.html')

def redirect_to_original_url(request, short_code):
    try:
        shortened_url = Url.objects.get(short_code=short_code)
        return redirect(shortened_url.original_url)
    except Url.DoesNotExist:
        return render(request, '404.html')

from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_shortened_url, name='create_shortened_url'),
    path('<short_code>/', views.redirect_to_original_url, name='redirect_to_original_url'),
]
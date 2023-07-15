from django.urls import path
from .views import index, top_sellers, register

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('register/', register, name='register')
]
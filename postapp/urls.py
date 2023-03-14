from .views import hello, greet,greet2
from django.urls import path

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('greet/', greet, name='greeting'),
    path('greet2/', greet2, name='greeting2')
]

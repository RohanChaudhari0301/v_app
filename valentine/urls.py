from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('yes/', views.yes_page, name='yes_page'),
    path('letter/', views.letter_page, name='letter_page'),
]

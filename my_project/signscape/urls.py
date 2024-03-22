from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Existing home page URL
    path('faq.html', views.faq, name='faq'),  # Define a new URL pattern for faq.html
    path('faq/', views.faq, name='faq'),
    
]
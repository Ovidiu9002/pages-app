from django.urls import path
from pages.views import HomePageView, AboutPage

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPage.as_view(), name='about')
]
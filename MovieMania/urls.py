from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'about.html'), name = 'about'),
    path('signup/',views.signup, name = 'signup'),
    path('test/', views.main, name = 'main'),
    path('wishlist/',views.wishlist, name = 'wishlist'),
    path('watchlater/', views.watchlater, name = 'watchlater'),
]
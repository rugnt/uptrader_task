from django.urls import path
from .views import menu_view, redirect_to_menu


urlpatterns = [
    path('', redirect_to_menu),
    path('menu/', menu_view, name='main_menu'),
    path('menu/<path:path>', menu_view, name='menu')
]
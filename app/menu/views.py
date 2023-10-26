from django.shortcuts import render, redirect
from django.http import Http404
from .models import TreeMenu


def menu_view(request, path=''):
    try:
        return render(request, 'menu/draw_menu.html', {'path': path})
    except TreeMenu.DoesNotExist:
        raise Http404


def redirect_to_menu(request):
    return redirect('main_menu')

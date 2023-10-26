from django.shortcuts import render, redirect


def menu_view(request, path=''):
    return render(request, 'menu/draw_menu.html', {'path': path})


def redirect_to_menu(request):
    return redirect('main_menu')

from django.http import HttpResponse

from django.shortcuts import render


def index(request):
    return render(request, 'posts/index.html')


def groups(request):
    return HttpResponse(
        '<h1> Список групп </h1> <h3> <ol>'
        '<li>Чемодан; </li> <li> Ручка: </li> </ol> </h3>'
    )


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request, all_slug):
    return HttpResponse(f'Пост номер {all_slug}')

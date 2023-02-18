from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def groups(request):
    return HttpResponse('Список групп')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request, all_slug):
    return HttpResponse(f'Пост номер {all_slug}')

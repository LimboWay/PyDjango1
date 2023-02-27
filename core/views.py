from django.http import HttpResponse
from django.shortcuts import render


def view_with_param(request, value):
    return HttpResponse(f'With param: "{value}"')


def view_without_param(request):
    return HttpResponse('Without param')


def index(request):
    return render(request, 'index.html')


def error_404(request, exception):
    context = {'page_title': '404'}
    response = render(request, 'includes/404.html', context=context)
    response.status_code = 404
    return response

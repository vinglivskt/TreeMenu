from django.db import connection
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView

from TreeMenuApp.models import Menu


class PageView(TemplateView):

    """ Представление индексной страницы, отображающее древовидное меню """

    template_name = "TreeMenuApp/index.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['menu'] = Menu.objects.filter(slug='main_menu').first()
        return context

    def get(self, request: HttpRequest, *args, **kwargs):

        response = super().get(request, *args, **kwargs)

        print("Количество запросов к базе данных: ", len(connection.queries))

        return response

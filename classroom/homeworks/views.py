from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from homeworks.models import Homework
from django.template import loader

# def index(request: HttpRequest) -> HttpResponse:
#     result = "<h1>Список заданий</h1>\n"
#     qs = Homework.objects.order_by("-created_at").all()
#     result += "<ul>\n"
#     for hw in qs:
#         result += "<li>\n"
#         result += f"<p>Тема: {hw.topic}</p>\n"
#         result += f"<p>Задание: {hw.name}</p>\n"
#         result += "</li>\n"
#     result += "</ul>\n"
#     return HttpResponse(result)


# def index(request: HttpRequest) -> HttpResponse:
#     template = loader.get_template('homeworks/index.html')
#     qs = Homework.objects.order_by("-created_at").all()
#     context = {"homeworks": qs}
#     return HttpResponse(template.render(context, request))


def index(request: HttpRequest) -> HttpResponse:
    qs = Homework.objects.order_by("-created_at").all()
    return render(request, "homeworks/index.html", {"homeworks": qs})





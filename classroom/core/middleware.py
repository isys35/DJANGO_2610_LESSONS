from django.http import HttpResponse


def simple_middleware(get_response):
    # Здесь можно вьmолнить какую-либо инициализацию

    def middleware(request):
        # Здесь выполняется обработка клиентского запроса
        print("Событие до контроллера")
        response = get_response(request)

        # Здесь выполняется обработка ответа
        print("Cобытие после контроллера")
        return response

    return middleware


class SimpleClassMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("До контроллера")
        response = self.get_response(request)
        print("После контроллера")
        return response

    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     print("Обработка представления")
    #     return view_func(request, *view_args, **view_kwargs)

    # def process_exception(self, request, exception):
    #     return HttpResponse(content=b"Error!!!!")

    #
    def process_template_response(self, request, response):

        print("Обработка шаблона")
        return response

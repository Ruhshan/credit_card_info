
from django.conf import settings


def CardActivityMiddleware(get_response):
    def middleware(request):
        global uid
        uid = request.user.pk
        settings.UIDX = uid
        response = get_response(request)
        return response

    return middleware


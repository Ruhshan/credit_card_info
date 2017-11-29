
from django.conf import settings
from cardinfo import models

def CardActivityMiddleware(get_response):
    def middleware(request):
        models.user_id = request.user.pk
        response = get_response(request)
        return response

    return middleware


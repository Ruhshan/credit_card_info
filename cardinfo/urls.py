from cardinfo.api import *
from django.conf.urls import *
from rest_framework import routers
router = routers.DefaultRouter(trailing_slash=True)
from . import views
from .api import CardRetrive
#router.register(r'', CardRetrive)

#urlpatterns = [url(r"^login2/", views.loginView)]

#urlpatterns = router.urls


urlpatterns = [url(r"", CardRetrive.as_view())]

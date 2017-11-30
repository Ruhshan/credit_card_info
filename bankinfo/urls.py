from bankinfo.api import *
from django.conf.urls import *
from rest_framework import routers
router = routers.DefaultRouter(trailing_slash=True)
from . import views
router.register(r'api', BankRetrive)

#urlpatterns = [url(r"^login2/", views.loginView)]

urlpatterns = router.urls


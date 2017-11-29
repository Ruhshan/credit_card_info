from bankinfo.api import *
from rest_framework import routers
router = routers.DefaultRouter(trailing_slash=False)

router.register(r'api', BankRetrive)
from django.conf.urls import *

urlpatterns = router.urls
from bankinfo.api import *
from rest_framework import routers
router = routers.DefaultRouter(trailing_slash=True)

router.register(r'api', BankRetrive)

urlpatterns = router.urls
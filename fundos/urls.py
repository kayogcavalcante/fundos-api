from rest_framework.routers import DefaultRouter
from fundos.views import FundoImobiliarioViewSet


app_name = 'fundos'

router = DefaultRouter(trailing_slash=False)
router.register(r'fundos', FundoImobiliarioViewSet)

urlpatterns = router.urls
from django.urls import path,include
from .views import PlantViewSet, HistoryPestViewSet, HistoryWaterViewSet
from rest_framework.routers import SimpleRouter, DefaultRouter
# app_name = 'pot'
# router = SimpleRouter(trailing_slash=True)

router = DefaultRouter()
router.register(r'plants', PlantViewSet, basename='plants')
router.register(r'historypest', HistoryPestViewSet, basename='historypest')
router.register(r'historywater', HistoryWaterViewSet, basename='historywater')

# urlpatterns = [
#     path('', include(router.urls)),
    
# ]
urlpatterns = router.urls
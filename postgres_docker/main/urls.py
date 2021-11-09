from rest_framework.routers import DefaultRouter

from .views import RequestViewSet, AnswerViewSet

app_name = "main"


router = DefaultRouter()
router.register("requests", RequestViewSet, basename="requests")
router.register("answer", AnswerViewSet, basename="answer")
urlpatterns = router.urls
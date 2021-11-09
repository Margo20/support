from rest_framework.viewsets import ModelViewSet

from .models import ClientRequestModel, AnswerModel
from .serializers import ClientRequestSerializer, AnswerSerializer


class RequestViewSet(ModelViewSet):
    queryset = ClientRequestModel.objects.all()
    serializer_class = ClientRequestSerializer


class AnswerViewSet(ModelViewSet):
    queryset = AnswerModel.objects.all()
    serializer_class = AnswerSerializer

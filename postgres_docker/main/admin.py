from django.contrib import admin

from .models import ClientRequestModel, AnswerModel

admin.site.register(ClientRequestModel)
admin.site.register(AnswerModel)

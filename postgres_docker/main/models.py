from django.db import models
# from authentication.models import UserModel


# ticket from user
class ClientRequestModel(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Имя")
    # user_name = models.ForeignKey(UserModel, on_delete=models.PROTECT, related_name='client_request', verbose_name="Email пользователя")
    request_client = models.CharField(max_length=50, blank=True, null=True, verbose_name="Заявка пользователя")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Когда и во сколько")
    STATUS_TICKETS = [("new_ticket", "new_ticket"), ("resolved", "resolved"), ("unresolved", "unresolved"),
                      ("frozen", "frozen"),
                      ]
    status = models.CharField(
        max_length=30,
        choices=STATUS_TICKETS,
        default="new_ticket",
        verbose_name="Статус",
    )
    class Meta:

        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ('-published',)

    def __str__(self):
        return f"{self.request_client}"


# support answer, correspondence
class AnswerModel(models.Model):
    client_request = models.ForeignKey(ClientRequestModel, blank=True, null=True, on_delete=models.PROTECT,
                                       verbose_name="Запрос пользователя", related_name='answers')
    client_text = models.TextField(blank=True, null=True, verbose_name="Текст пользователя")
    support_text = models.TextField(blank=True, null=True, verbose_name="Текст саппорт")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Когда и во сколько")

    class Meta:
        verbose_name = "Ответ на заявку"
        verbose_name_plural = "Ответы на заявки"

    def __str__(self):
        # return  (self.status, self.client_text, self.support_text)
        return '%s: %s' % (self.client_text, self.support_text)

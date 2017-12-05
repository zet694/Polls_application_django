from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    quest_text = models.CharField(max_length=200, verbose_name="Текст вопроса")
    pub_date = models.DateTimeField("Дата публикации")

    class Meta:
        verbose_name_plural = "Вопросы"
        verbose_name = "Вопрос"

    def __str__(self):
        return self.quest_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name="Ответ")
    votes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Ответы"
        verbose_name = "Ответ"

    def __str__(self):
        return self.choice_text

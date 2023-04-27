from django.db import models
from quizzes.models import Quiz
from django.contrib.auth.models import User


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='Test')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Foydalanuvchi')
    score = models.FloatField(verbose_name="Bal")

    def __str__(self):
        return f"{self.pk}"

    class Meta:
        verbose_name = 'Natija'
        verbose_name_plural = 'Natijalar'
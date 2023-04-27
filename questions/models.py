from django.db import models
from quizzes.models import Quiz


class Question(models.Model):
    text = models.CharField(max_length=200, verbose_name='Savol')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name="Test")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')

    def __str__(self):
        return f"{self.text}"

    def get_answers(self):
        return self.answer_set.all()

    class Meta:
        verbose_name = 'Savol'
        verbose_name_plural = 'Savollar'


class Answer(models.Model):
    text = models.CharField(max_length=200, verbose_name='Javoblar variantlari')
    correct = models.BooleanField(default=False, verbose_name="To'gri javob")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Savol')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"

    class Meta:
        verbose_name = 'Javob'
        verbose_name_plural = 'Javoblar'
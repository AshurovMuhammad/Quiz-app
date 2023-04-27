from django.db import models
import random

DIFF_CHOICES = (
    ('easy', 'oson'),
    ('medium', "o'rta"),
    ('hard', 'murakkab'),
)


class Quiz(models.Model):
    name = models.CharField(max_length=120, verbose_name='Test nomi')
    topic = models.CharField(max_length=120, verbose_name='Mavzusi')
    number_of_questions = models.IntegerField(verbose_name='Savollar miqdori')
    time = models.IntegerField(help_text='Sinov davomiyligi daqiqalarda', verbose_name='Sinov muddati')
    required_score_to_pass = models.IntegerField(help_text='Majburiy ball %da', verbose_name="O'tish uchun bal")
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES, verbose_name='Murakkablik')

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Testlar'
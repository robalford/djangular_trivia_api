from django.db import models


class Question(models.Model):
    category = models.CharField(max_length=50)
    question = models.TextField()

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.TextField()
    is_correct = models.BooleanField()

    class Meta:
        ordering = ['answer', ]

    def __str__(self):
        return self.answer

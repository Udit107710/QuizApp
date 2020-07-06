from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=120)


class Answer(models.Model):
    option = models.CharField(max_length=30)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

# class QuestionAnswer(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
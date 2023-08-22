from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=150)
    pub_date = models.DateTimeField()
    
class Choice(models.Model):
    choice_text = models.CharField(max_length=150)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.PositiveSmallIntegerField()
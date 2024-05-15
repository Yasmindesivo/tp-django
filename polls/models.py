from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.question_text #No llamamos la función porque django lo hace solo, en views si hay que llamarla

        
class Answer(models.Model):
    answer_text = models.CharField(max_length=200)
    date = models.DateTimeField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.answer_text_
    
    def is_popular(self):
        return self.likes >= 3

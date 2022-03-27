from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)  #   제목
    content = models.TextField()                #   내용
    create_date = models.DateTimeField()        #   작성일시

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    # PK
    content = models.TextField()                                        # 답변내용
    create_date = models.DateTimeField()                                # 답변일시
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser

# Create your models here.
# class User(AbstractUser):
#     email = models.EmailField(
#         verbose_name='email',
#         max_length=255,
#         unique=True
#     )

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
    
    
class Board(models.Model):
    board_no = models.AutoField(primary_key=True)                       # 게시판 번호
    title = models.CharField(max_length=200, verbose_name='글 제목', help_text='100자 이내')                                    # 게시글 제목
    content = models.TextField()                                        # 게시글 내용
    create_date = models.DateTimeField()                                # 게시판 날짜
    
    
# ALTER TABLE auth_user ADD birth char(8) NULL;
# ALTER TABLE auth_user ADD nickname varchar(25) NULL;
# ALTER TABLE auth_user ADD tel varchar(25) NULL;
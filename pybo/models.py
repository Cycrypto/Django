from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)  # 제목
    content = models.TextField()            # 내용
    create_date = models.DateTimeField()    # 작성 일시

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE)   # Question의 FOREIGNKEY 이므로 질문글이 삭제되면 답글도 자동으로 삭제된다.
    content = models.TextField()
    create_date = models.DateTimeField()

# 장고 속성
# docs.djangoproject.com/en/3.0/ref/models/fields/#field-types

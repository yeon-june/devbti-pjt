from django.db import models

class Question(models.Model):
    title = models.TextField()
    choice_right = models.TextField()
    choice_left = models.TextField()
    question_category = models.TextField()

class Mbti(models.Model):
    mbti_name = models.TextField()
    title = models.TextField()
    mbti_type = models.TextField()
    best_mbti = models.IntegerField(default=0)
    worst_mbti = models.IntegerField(default=0)
    top_image = models.ImageField(null=True, blank=True)
    view_cnt = models.IntegerField(default=0)

class BaseInfo(models.Model):
    mbti = models.ForeignKey( 
        Mbti,
        on_delete=models.CASCADE,
        related_name= 'base_info'
    )
    content = models.TextField()

class Howto(models.Model):
    mbti = models.ForeignKey(
        Mbti,
        on_delete=models.CASCADE,
        related_name= 'how_to'
    )
    content = models.TextField()
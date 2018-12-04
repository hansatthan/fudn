from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=50, default='SOME STRING')
    comment = models.CharField(max_length=200)
    predict = models.CharField(max_length=20)


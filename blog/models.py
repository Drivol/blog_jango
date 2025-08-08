from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitulo = models.TextField()
    informações = models.TextField()


def __str__(self):
    return self.title
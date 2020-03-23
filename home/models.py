from django.db import models


class Contactt(models.Model):
    email = models.EmailField(max_length=30)
    name = models.CharField(max_length=30)
    text = models.TextField()

    # def __str__(self):
    #     return self.title

from django.db import models

# Create your models here.

class Memo(models.Model):
    user = models.CharField(max_length=10)
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title
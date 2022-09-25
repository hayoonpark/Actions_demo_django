from django.db import models

# Create your models here.

class Memo(models.Model):
    title = models.CharField(max_length=30)
    user = models.CharField(max_length=10)

    def __str__(self):
        return self.title
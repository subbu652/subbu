from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=40, default='Not started')
    due_date = models.DateField()

    def __str__(self):
        return self.title
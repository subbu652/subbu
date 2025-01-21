from django.db import models

# Create your models here.
class SigninTable(models.Model):
    user_name = models.CharField(max_length=150,unique=True)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} signed in at {self.date_time}"

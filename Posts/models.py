from django.db import models

# Create your models here.
class SignUp(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    email=  models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.email

class News(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
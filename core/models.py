from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=35)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Job(models.Model):
    title = models.CharField(max_length=20)
    company = models.CharField(max_length=10)
    posted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
class Application(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user}->{self.job}"
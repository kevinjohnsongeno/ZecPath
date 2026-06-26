from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=35)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Employer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="employer")
    company_name = models.CharField(max_length=50)
    def __str__(self):
        return self.company_name
class Candidate(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="candidate")
    resume = models.FileField(upload_to="resumes/",blank=True,null=True)
    def __str__(self):
        return self.user.name
class Job(models.Model):
    employer = models.ForeignKey(Employer,on_delete=models.CASCADE,related_name="job")
    title = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    posted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
class Application(models.Model):
    candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE,related_name="application")
    job = models.ForeignKey(Job,on_delete=models.CASCADE,related_name="application")
    applied_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.candidate.user.name}->{self.job.title}"
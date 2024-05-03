from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField()
  image = models.ImageField(upload_to='category')

  def __str__(self):
    return self.title
  


class Contact(models.Model):
  name = models.CharField(max_length=30)
  email = models.EmailField()
  subject = models.CharField(max_length=50)
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True, )

  def __str__(self):
    return self.name
   
class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
  geneder_choices = (
    ('male','Male'),
    ('female','Female'),
    ('other','Other')
  )
  name = models.CharField(max_length=50)
  corporate = models.CharField(max_length=50)
  position = models.CharField(max_length=50)
  my_skills_choices = (
    ('marketing','Marketing'),
    ('project_management','Project Management'),
    ('customer service','customer service'),
    ('software development','Software Development'),
  )
  my_skills = models.CharField(max_length=50,default='software development')  
  needed_skills = models.TextField(max_length=50,default='software development')
  free_time = models.TimeField()
  bio = models.CharField(max_length=200,default=1)
  gender= models.CharField(max_length=10,choices=geneder_choices)
  image = models.ImageField(upload_to='profiles')
  age = models.IntegerField()
  email = models.EmailField()
  # photo = models.ImageField(upload_to='profiles')

  def __str__(self):
    return self.name
   
class Skill(models.Model):
  skill_choices = (
    ('marketing','Marketing'),
    ('project_management','Project Management'),
    ('customer service','customer service'),
    ('software development','Software Development'),
  )
  user = models.CharField(max_length=50)
  skill= models.CharField(max_length=50,choices=skill_choices)
  experience = models.IntegerField(default=1)
  def __str__(self):
    return self.user
  

class Workdemo(models.Model):
  user = models.CharField(max_length=50)
  image = models.ImageField(upload_to='workdemo')
  video = models.FileField(upload_to='workdemo')
  file = models.FileField(upload_to='workdemo')

  def __str__(self):
    return self.user
  


  
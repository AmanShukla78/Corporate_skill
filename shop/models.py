from django.db import models

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
  geneder_choices = (
    ('male','Male'),
    ('female','Female'),
    ('other','Other')
  )
  name = models.CharField(max_length=50)
  corporate = models.CharField(max_length=50)
  position = models.CharField(max_length=50)
  exchange = models.CharField(max_length=50)
  free_time = models.DateTimeField(editable=True)
  gender= models.CharField(max_length=10,choices=geneder_choices)
  image = models.ImageField(upload_to='profiles')

  def __str__(self):
    return self.name
   
class Skill(models.Model):
  skill_choices = (
    ('marketing','Marketing'),
    ('project_management','Project Management'),
    ('customer service','customer service'),
  )
  user = models.CharField(max_length=50)
  skill= models.CharField(max_length=50,choices=skill_choices)
  experience = models.DateField(editable=True)
  def __str__(self):
    return self.user
  

class Workdemo(models.Model):
  user = models.CharField(max_length=50)
  image = models.ImageField(upload_to='workdemo')
  video = models.FileField(upload_to='workdemo')
  file = models.FileField(upload_to='workdemo')

  def __str__(self):
    return self.user
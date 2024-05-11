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
   
# class Skill(models.Model):
#   skill_choices = (
#     ('marketing','Marketing'),
#     ('project_management','Project Management'),
#     ('customer service','customer service'),
#     ('software development','Software Development'),
#   )
#   user = models.CharField(max_length=50)
#   skill= models.CharField(max_length=50,choices=skill_choices)
#   experience = models.IntegerField(default=1)
#   def __str__(self):
#     return self.user
  

class Workdemo(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='workdemo', null=True, blank=True)
  video = models.FileField(upload_to='workdemo', null=True, blank=True)
  file = models.FileField(upload_to='workdemo', null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.user
  
# class to invite other users to be skill partners
class Invite(models.Model):
  invite_choices = (
    ('accepted','Accepted'),
    ('rejected','Rejected'),
    ('pending','Pending'),
  )
  userA = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inviteA')
  userB = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inviteB')
  invite_status = models.CharField(max_length=50,choices=invite_choices)
  created_at = models.DateTimeField(auto_now_add=True, )
  def __str__(self):
    return self.user
  
class Chat(models.Model):
  userA = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userchatA')
  userB = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userchatB')
  msgby = models.ForeignKey(User, on_delete=models.CASCADE, related_name='msgby')
  message = models.TextField()
  is_read = models.BooleanField(default=False) 
  created_at = models.DateTimeField(auto_now_add=True, )
  def __str__(self):
    return f'{self.userA} - {self.userB}'
  
class VideoSession(models.Model):
  userA = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userVidA')
  userB = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userVidB')
  created_at = models.DateTimeField(auto_now_add=True, )
  def __str__(self):
    return f'{self.userA} - {self.userB}'
  
class Notification(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  message = models.TextField()
  is_read = models.BooleanField(default=False) 
  created_at = models.DateTimeField(auto_now_add=True, )
  def __str__(self):
    return self.user
  
class ShareSkill(models.Model):
  status_choices = (
    ('pending','Pending'),
    ('learning','Learning'),
    ('completed','Completed'),
  )
  userA = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userSkillA')
  userB = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userSkillB')
  skillA = models.CharField(max_length=50)
  skillB = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True, )
  def __str__(self):
    return f'{self.userA} - {self.userB}'
  
class Report(models.Model):
  userA = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userReportA')
  userB = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userReportB')
  complain = models.TextField()
  screenshot = models.ImageField(upload_to='reports')
  created_at = models.DateTimeField(auto_now_add=True, )
  def __str__(self):
    return f'{self.userA} - {self.userB}'


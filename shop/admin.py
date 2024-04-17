from django.contrib import admin
from .models import Category,Contact,Profile,Skill,Workdemo


# Register your models here.
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Workdemo)
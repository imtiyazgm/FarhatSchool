from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse

# Create your models here.
class subName(models.Model):
    Subject_Name = models.CharField(max_length=255)
  
    def __str__(self):
        return self.Subject_Name

    def get_absolute_url(self):
        return reverse ('dashboard') 


class gradeName(models.Model):
    Grade_Name = models.CharField(max_length=255)
   
    def __str__(self):
        return self.Grade_Name 

    def get_absolute_url(self):
        return reverse ('dashboard') 


class docType(models.Model):
    Notes_Type = models.CharField(max_length=255)
  
    def __str__(self):
        return self.Notes_Type

    def get_absolute_url(self):
        return reverse ('dashboard') 


class notes(models.Model):
    chapterName = models.CharField(max_length=255)
    GradeName = models.ForeignKey(gradeName, null=True, on_delete=models.SET_NULL)
    Subject = models.ForeignKey(subName, default=0,null=True,  on_delete=models.SET_NULL)
    NotesType = models.CharField(max_length=255)
    Notesfile = models.FileField(upload_to='Class/Notes/', max_length=100)
    
    def __str__(self):
        return self.chapterName + '|' + str(self.GradeName) + '|' + str(self.NotesType)

    def get_absolute_url(self):
        return reverse ('dashboard') 


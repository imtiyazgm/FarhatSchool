from django import forms


from django.forms import widgets
from django.forms.models import ModelForm

from django.utils.regex_helper import Choice
from django.db.models import fields
from django .forms import ModelForm, fields, widgets
from .models import *

class SubForm(ModelForm):
    class Meta:
        model = subName
        fields = '__all__'
        

class TagForm(ModelForm):
    class Meta:
        model = docType
        fields = '__all__'    


choices = docType.objects.all().values_list('Notes_Type','Notes_Type')
choice_List =[]

for item in choices:
    choice_List.append(item)

class AddNotesForm(forms.ModelForm):
    class Meta:
        model = notes
        fields = ('chapterName', 'GradeName', 'Subject', 'NotesType', 'Notesfile')
        widgets = {
            'chapterName' : forms.TextInput(attrs={'class':'form-control'}),
            'GradeName' : forms.Select(attrs={'class':'form-control'}),
            'Subject' : forms.Select(attrs={'class':'form-control'}),
            'NotesType' : forms.Select(choices=choice_List, attrs={'class':'form-control'}),
            'Notesfile' : forms.FileInput(attrs={'class':'form-control'}),
                           
        }

class EditNotesForm(forms.ModelForm):
    class Meta:
        model = notes
        fields = ['chapterName', 'GradeName', 'Subject', 'NotesType', 'Notesfile']
        


class EditGradeForm(forms.ModelForm):
    class Meta: 
        model = gradeName
        fields = '__all__'
        
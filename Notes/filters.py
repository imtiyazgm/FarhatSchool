from django.db.models import fields
from django.db.models.fields import files
import  django_filters 
from .models import *

class NotesFilter(django_filters.FilterSet):
    class Meta:
        model = notes
        files = '__all__'
        exclude = ['Notesfile']
        

class GradeFilter(django_filters.FilterSet):
    class Meta:
        model = notes
        fields = '__all__'
        exclude = ['GradeName', 'Notesfile' ]

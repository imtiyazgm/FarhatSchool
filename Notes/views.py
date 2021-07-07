from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import SubForm, TagForm, AddNotesForm,  EditNotesForm, EditGradeForm
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .filters import NotesFilter, GradeFilter

# Create your views here.
def home(request):
    notesList = notes.objects.all()
    Total_Notes = notesList.count()

    gradeList = gradeName.objects.all()
    Total_Grade = gradeList.count()

    subList = subName.objects.all()
    Total_sub = subList.count()

    docTypeList = docType.objects.all()
    T_Dtype = docTypeList.count()
    
    myfilter = NotesFilter(request.GET, queryset = notesList )
    notesList = myfilter.qs



    context = {'notesList':notesList, 'myfilter':myfilter, 'Total_Notes':Total_Notes, 'Total_sub':Total_sub, 'Total_Grade':Total_Grade, 'T_Dtype':T_Dtype }
    return render(request, 'Notes/dashboard.html' , context)


#Disply the Grade List
def Grade_List(request):
    gradeList = gradeName.objects.all()
    context = {'gradeList':gradeList }
    return render (request, 'Notes/List_Grade.html', context)


#Disply the Doctype List
def Cat_List(request):
    catlist = docType.objects.all()
    context = {'catlist':catlist }
    return render (request, 'Notes/List_Category.html', context)


#Disply Subject list using Genric (listView) method 
class Sub_List(ListView):
    model = subName
    template_name = 'Notes/List_Sub.html'


# Add Subject create by using function based view method --------------------------
def AddSub(request):
    form = SubForm()
    if request.method == 'POST':
        form = SubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

       
    context ={'form':form}
    return render(request, 'Notes/AddSub_form.html', context )

 # EDit Subject create by using function based view method 
def EditSub(request, pk):
    subList = subName.objects.get(id=pk)
    
    form = SubForm(instance=subList)
    if request.method == 'POST':
        form = SubForm(request.POST, instance=subList)
        if form.is_valid():
            form.save()
            return redirect('SubList')

    
    context = {'form':form}
    return render(request, 'Notes/AddSub_form.html', context )
#-------------------------- End Subject-------------------



# Add Grade  by using generic method ---------------------
class AddGradeView(CreateView):
    model = gradeName
    fields = '__all__'
    template_name = 'Notes/AddGrade.html'

            # this edit Grade using genric class
class EditGradeView(UpdateView,):
    model = gradeName
    form_class = EditGradeForm
    template_name = 'Notes/UpdateGrade.html'
    #fields= '__all__'
    success_url = reverse_lazy('GradeList')

            # List of Notes on click of Grade 

def GNoteList(request, pk):
    grade = gradeName.objects.get(id=pk)
    GradeNoteList = grade.notes_set.all()

    Gfilter = GradeFilter(request.GET, queryset=GradeNoteList)
    GradeNoteList = Gfilter.qs

   
    context = {'GradeNoteList':GradeNoteList, 'Gfilter':Gfilter}

    return render (request, 'Notes/List_Grade_Notes.html', context )



# End Grade---------------------- 


# Add Notes  by using generic method 
class AddNotesView(CreateView):
    model = notes
    form_class = AddNotesForm
    template_name = 'Notes/AddNotes.html'
    #fields = '__all__'


# this edit and delete is perfomred here using genric class
class NotesUpdateView(UpdateView,):
    model = notes
    form_class = EditNotesForm
    template_name = 'Notes/UpdateNotes.html'
    #fields= '__all__'
    success_url = reverse_lazy('dashboard')

class DeleteNotes(DeleteView):
    model = notes
    template_name = 'Notes/delete_Notes.html'
    success_url = reverse_lazy('dashboard')


# Tag / Category ........................................................................ 


# add Tag / Category 
def AddTag(request):
    form = TagForm()
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
      
    context ={'form':form}
    return render(request, 'Notes/AddTag_form.html', context )

# EDIT CATEGORY .....
def EditTag(request, pk):
    docTypeList = docType.objects.get(id=pk)
        
    form = TagForm(instance=docTypeList)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=docTypeList)
        if form.is_valid():
            form.save()
            return redirect('CatList')

    
    context = {'form':form}
    return render(request, 'Notes/AddTag_form.html', context )


# Delete CATEGORY 
class DeleteTag(DeleteView):
   
    model = docType
    template_name = 'Notes/delete_Cat.html'
    success_url = reverse_lazy('CatList')


# ............END Tag / Category ..............................................


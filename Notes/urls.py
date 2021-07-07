from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from .views import AddGradeView, AddNotesView, Sub_List, Cat_List, NotesUpdateView, DeleteNotes, EditGradeView, DeleteTag


urlpatterns = [
        path('dashboard/', views.home, name='dashboard'),
        path('AddSub/', views.AddSub, name='Add_Sub'), 
        path('Add_Tag/', views.AddTag, name='Add_Tag'),        
        path('CatList/', views.Cat_List, name='CatList'),        
        path('GradeList/', views.Grade_List, name='GradeList'),        
        path('AddGrade/', AddGradeView.as_view(), name='Add_Grade'),
        path('AddNotes/', AddNotesView.as_view(), name='Add_Notes'),
        path('NotesUpdate/<str:pk>/', NotesUpdateView.as_view(), name='NotesUpdate'),
        path('Delete_Notes/<str:pk>/', DeleteNotes.as_view(), name='Delete_Notes'),
        path('EditGrade/<str:pk>/', EditGradeView.as_view(), name='EditGrade'),
        path('G_NoteList/<str:pk>/', views.GNoteList, name='G_NoteList'), 
        path('SubList/', Sub_List.as_view(), name='SubList'),
        path('Edit_Sub/<str:pk>/', views.EditSub, name='Edit_Sub'),
        path('Edit_Tag/<str:pk>/', views.EditTag, name='Edit_Tag'),
        path('Delete_Tag/<str:pk>/', DeleteTag.as_view(), name='Delete_Tag'),
         
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

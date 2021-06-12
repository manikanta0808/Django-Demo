from django.urls import path
from .views import *

urlpatterns = [
    path('',indexView, name='index'),
    path('blog/',blog,name='blog'),
    path('sum/',sum, name = 'sum'),
    path('StudentSubmission/',StudentSubmission,name='StudentSubmission'),
    path('FacultySubmission/', FacultySubmission, name='FacultySubmission'),
]
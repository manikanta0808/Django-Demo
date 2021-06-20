from django.urls import path
from .views import *

urlpatterns = [
    # path('blogView/',indexView, name='index'),
    path('',blogView,name='blogView'),
    path('sum/',sum, name = 'sum'),
    path('sumView/', sumView, name = 'sumView'),
    path('StudentSubmission/',StudentSubmission,name='StudentSubmission'),
    path('FacultySubmission/', FacultySubmission, name='FacultySubmission'),
]
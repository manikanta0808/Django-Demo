from django.shortcuts import render
from .models import Faculty, Department, Work, Students
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

# cross site request forgery
# Create your views here.
def indexView(request):
    return render(request, 'index.html')


def sum(request):
    if request.method == 'POST':
        
        firstname = request.POST['a']
        lastname = request.POST['b']
        
        return render(request,'result.html',{
            'first' : firstname,
            'last' : lastname
        })
    




@csrf_protect
def StudentSubmission(request):
    if request.method == 'POST':
        name = request.POST['name']
        id = request.POST['id']
        dept = request.POST['dept']
        year = request.POST['year']
        try:
            obj = Students.objects.get(sid = id)
        except Students.DoesNotExist:
            dep = Department.objects.get(name = dept)
            obj = Students(sid = id,name = name,year= year, did = dep)
            obj.save()
            print('saved')
    return render(request, 'student.html')

@csrf_protect
def FacultySubmission(request):
    if request.method == 'POST':
        faculty = request.POST['faculty']
        dept = request.POST['dept']
        try:
            obj = Faculty.objects.get(name = faculty)
            
        except Faculty.DoesNotExist:
            obj = Faculty(name = faculty)
            obj.save()
        try:
            dep = Department.objects.get(name = dept)
            p = Faculty.objects.get(name = faculty)
            if not Work.objects.filter(fid = p,did = dep).exists():
                workobj = Work(fid = p, did = dep)
                workobj.save()
            else:
                print('Already an entry exist')

        except Department.DoesNotExist:
            print("Entered Department don't exist")

        
    return render(request, 'index.html')


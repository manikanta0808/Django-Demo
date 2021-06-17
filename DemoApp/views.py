from django.shortcuts import render
from .models import Faculty, Department, Work, Students, BlogModel
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

# cross site request forgery
# Create your views here.
def indexView(request):
    return render(request, 'temp.html')

# def blog(request):
#     return render(request, 'blog.html')


def sum(request):
    if request.method == 'POST':
        
        firstname = request.POST['a']
        lastname = request.POST['b']
        
        return render(request,'result.html',{
            'first' : firstname,
            'last' : lastname
        })

    elif request.method == "GET":
        pass 

    elif request.method == "PUT":
        passaction="/sum/"
    

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
3

def convert_to_json(obj):
    return {
        'author' : obj.author,
        'content' : obj.content
    }

def blogView(request):
    try:
        content = BlogModel.objects.all()
        contents = []
        for cont in content:
            contents.append(convert_to_json(cont))
        print(contents)
        return render(request, 'blog.html',{
            'content' : contents
        })
    except BlogModel.DoesNotExist:
        print('No content exist')
    


'''    
        
        Faculty                     Department
       
    fid      name               did             name
    1        Sayed               1              CSE
    2        Mani                2               IT
    3        Uday                3              ECE
    4        Ramesh              4              EEE
    5        Rajesh              5              MEC

        WORKS

        
    fid     did
    1       1
    1       3
    5       5
    
    {
        'mid' : 1,
        'author' : 'john',
        'content' : 'Hi every one'
    }
    json.stringify()

'''
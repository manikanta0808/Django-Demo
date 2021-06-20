from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.
# models are the tables in database

class Department(models.Model):
    did = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    fid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    # did = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Work(models.Model):
    fid = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    did = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fid} works in {self.did}'

class Students(models.Model):
    sid = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=35)
    year = models.IntegerField(default=1)
    did = models.ForeignKey(Department, on_delete=SET_NULL,null=True)

    def __str__(self):
        return self.sid


class SecurityGuard(models.Model):
    sid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)  

    def __str__(self):
        return self.name


class BlogModel(models.Model):
    mid = models.IntegerField(primary_key=True)
    author  = models.CharField(max_length=35)
    content = models.TextField()

    def __str__(self):
        return self.author


'''
                BlogModel

            mid     author     content
            1       Sayed       Hi there , I'm new here.
            2       Mani        Hello Sayed, Good to see you here.

            render(request, 'template', {

            }, context_type = 'json')
'''
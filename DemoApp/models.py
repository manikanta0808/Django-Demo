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


'''
        WORKS

    fid     did
    1       1
    1       3
    1       NULL

'''
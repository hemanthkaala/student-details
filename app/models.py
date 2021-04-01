from django.db import models

# Create your models here.
class Student(models.Model):
    s_name=models.CharField(max_length=40,primary_key=True)

class S_Subjects(models.Model):
    s_name=models.ForeignKey(Student,on_delete=models.CASCADE)
    subject1=models.CharField(max_length=100)
    subject2=models.CharField(max_length=100)

class S_Marks(models.Model):
    s_name=models.ForeignKey(Student,on_delete=models.CASCADE)
    subject1=models.ForeignKey(S_Subjects,on_delete=models.CASCADE)
    subject1_marks=models.IntegerField(max_length=3)
    date=models.DateField(auto_now=True)


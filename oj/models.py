from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField, DateTimeField
from datetime import datetime

# class User(models.Model):
#     Username= models.CharField(max_length=50)
#     Password= models.CharField(max_length=50)

class Problem(models.Model):
    problem_name= models.CharField( max_length=100)
    description= models.CharField( max_length=500)
    status= models.CharField(max_length=10)
    def __str__(self):
        return self.problem_name

class testcases(models.Model):
    problem_id= models.ForeignKey(Problem, on_delete=models.CASCADE)
    input= models.CharField(max_length=200)
    output= models.CharField( max_length=200)

    

class Submission(models.Model):
    problem_id=models.ForeignKey(Problem, on_delete=models.CASCADE)
    verdict= models.CharField(max_length=30)
    submit_time= models.DateTimeField

    def __str__(self):
        return self.verdict
# Create your models here.

from django.contrib import admin
from oj.models import Problem, testcases,Submission
# Register your models here.
admin.site.register(Problem)
admin.site.register(testcases)
admin.site.register(Submission)
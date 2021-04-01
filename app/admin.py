from django.contrib import admin

# Register your models here.
from app.models import *
admin.site.register(Student)
admin.site.register(S_Subjects)
admin.site.register(S_Marks)

from django.contrib import admin
from .models import student

@admin.register(student)
class studentadmin(admin.ModelAdmin):
    list_display=('id','name','email','password','phone')


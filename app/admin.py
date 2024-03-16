from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ["user", "mobile", "status"]
    list_editable = ["status", ]
    
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["name", "level", "language"]
    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["user", "NNI", "mobile", "diplome", "langue", "status"]
    list_editable = ["status", ]
    
@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ["manager", "name", "address", "status"]
    list_editable = ["status", ]
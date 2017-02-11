from django.contrib import admin
from Homework.models import *
# Register your models here.
class HomeworkAdmin(admin.ModelAdmin):
    pass

class CourseAdmin(admin.ModelAdmin):
    pass

class Homework_itemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Homework, HomeworkAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Homework_item, Homework_itemAdmin)

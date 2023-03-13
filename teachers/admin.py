from django.contrib import admin
from teachers.models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'salary')
    list_per_page = 15
    readonly_fields = ('created', 'updated')

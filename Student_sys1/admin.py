from django.contrib import admin
from Student_sys1.models import students,teachers,course_1
# Register your models here.
#admin.site.register(students,teachers,course_1)不允许传入三个
admin.site.register(students)
admin.site.register(teachers)
admin.site.register(course_1)

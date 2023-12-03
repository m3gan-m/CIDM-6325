from django.contrib import admin

# Register your models here.
from checklistform.models import (WTStaff, Course,
                            Professor, Student, Reviewer)
# Register your models here.
admin.site.register(WTStaff)
admin.site.register(Course)
admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(Reviewer)

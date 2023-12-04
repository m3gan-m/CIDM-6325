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

#for comparison to old code
#from reviews.models import (Publisher, Contributor,
#                            Book, BookContributor, Review)
# Register your models here.
#admin.site.register(Publisher)
#admin.site.register(Contributor)
#admin.site.register(Book)
#admin.site.register(BookContributor)
#admin.site.register(Review)
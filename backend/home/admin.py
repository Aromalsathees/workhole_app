from django.contrib import admin
from . models import *


admin.site.register(UserContact)



# subjects models starts here 
admin.site.register(Subjects)
admin.site.register(DifferentSubjects)
admin.site.register(PopularSubjects)
admin.site.register(ToprelatedSubjects)
admin.site.register(Downloadmaterials)
# subjects models ends here


# exams models ends here
admin.site.register(Exams)
admin.site.register(DifferentExams)
admin.site.register(PopularExams)
admin.site.register(ToprelatedExams)
# exams models ends here


# course models starts from here 
admin.site.register(Courses)
admin.site.register(DifferentCourses)
admin.site.register(PopularCourses)
admin.site.register(ToprelatedCourses)
# courses models ends here



from django.contrib import admin
from django.urls import path

# Methods in the projects views and students views will in principle 
# be the same because of what they do behind the scenes in a database
# - CRUD
# It is common for developers to recyle the names of such functions
# - Let's explore some of the techniques to solve this

from students.views import new, student_list, detail, edit, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/new/', new, name='new-student'),
    # <noun-in-plural>/new or create

    # individual resource e.g. a specific student
    # <noun-in-plural>/<resource id>/<some action>/

    path('students/<int:id>/edit/', edit, name='edit-student' ),
    path('students/создавать/', new, name='create-student-ru'), 
    path('students/Müller/', new, name='create-student-ae'), 
    path('students/', student_list, name='home'),
    # details of a student (1 student)
    path('students/<int:id>/', detail, name='student-detail'),    
    path('students/<int:id>/delete/', delete, name='delete-student'),
]

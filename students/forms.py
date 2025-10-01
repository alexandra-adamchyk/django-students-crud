from django.forms import ModelForm
from students.models import Student


class StudentForm(ModelForm):
    class Meta:
        # reference to the table (MAGIC!!! 🧙)
        model = Student

        # fields/columns in a table we want to change
        fields = ['first_name', 'last_name', 'nickname', 'bio']
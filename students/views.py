from django.shortcuts import render, redirect
from django.http import HttpResponse
from students.models import Student
from students.forms import StudentForm
# Create your views here together with the teacher during code along.
# - index (show all entities in the database)
# - detail (show details of a single entity)
# - edit (load form to edit)
# - delete 
# - new (creating a new entity/resource)

# Create a new student
def new(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        # check that details are valid in the form e.g. missing data, etc.
        if form.is_valid():
            student = form.save()
            return redirect(f'/students/{student.id}/')
        else:
            # Here the frontend developer would display errors on the page
            return HttpResponse("There are some errors!!")
    else:
        form = StudentForm()
        return render(request, 'students/new.html', {'form': form})



def student_list(request):
    return render(request, 'students/index.html', {'students': Student.objects.all().order_by('first_name')})


def detail(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'students/detail.html', {'student': student})



def edit(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            updated_student = form.save()
            return redirect(f'/students/{updated_student.id}/')
        else:
            return HttpResponse("Sorry, try again!!")
    else:
        form = StudentForm(instance=student)
        return render(request, 'students/edit.html', {'student': student, 'form': form})

def delete(request, id):
    Student.objects.get(id=id).delete()
    # backend devs --> frontend developer (communicate with customer)
    return redirect('/students/')
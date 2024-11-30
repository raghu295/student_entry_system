from rest_framework import viewsets
from .forms import StudentForm
from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import render, redirect


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer




def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student_app/student_form.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_app/student_list.html', {'students': students})

def student_update(request, pk):
    student = Student.objects.get(pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student_app/student_form.html', {'form': form})

def student_delete(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_app/student_confirm_delete.html', {'student': student})
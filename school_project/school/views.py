from django.shortcuts import render
from .models import Student, Teacher, Class
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def get_all_students(request):
    students = Student.objects.all()
    template = loader.get_template("students_list.html")
    context = {"students": students}
    return HttpResponse(template.render(context, request))


def get_student(request, id):
    student = Student.objects.get(id=id)
    template = loader.get_template("student_detail.html")
    context = {"student": student}
    return HttpResponse(template.render(context, request))

def get_all_teachers(request):
    teachers = Teacher.objects.all()
    template = loader.get_template("teachers_list.html")
    context = {"teachers": teachers}
    return HttpResponse(template.render(context, request))


def get_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    template = loader.get_template("teacher_detail.html")
    context = {"teacher": teacher}
    return HttpResponse(template.render(context, request))

def get_all_classes(request):
    classes = Class.objects.all()
    template = loader.get_template("classes_list.html")
    context = {"classes": classes}
    return HttpResponse(template.render(context, request))


def get_class(request, id):
    class_obj = Class.objects.get(id=id)
    template = loader.get_template("class_detail.html")
    context = {"class": class_obj}
    return HttpResponse(template.render(context, request))

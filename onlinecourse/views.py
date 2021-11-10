from django.shortcuts import render
from .models import Course

def index(request):
    courses=Course.objects.all()
    context = {
        'course_list':courses
    }
    return render(request,'onlinecourse/course_list.html', context)



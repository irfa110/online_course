from django.shortcuts import render, HttpResponse,redirect
from .models import Course, Video

def home(request):
    courses = Course.objects.all()
    return render(request,'home.html',{'courses':courses})

def coursepage(request,slug):
    course = Course.objects.get(slug=slug)
    serial_number = request.GET.get('lecture',1)
    videos = course.video_set.all().order_by("serial_number")
    video = Video.objects.get(serial_number = serial_number,cource = course)

    if ((request.user.is_authenticated is False) and (video.is_preview is False)):
        return redirect("login")
    context = {
        'course':course,
        'video':video,
        'videos':videos,
    }
    return render(request,'course_page.html',context=context)

def checkout(request,slug):
    course = Course.objects.get(slug=slug)
    if not request.user.is_authenticated:
        return redirect("login")
    context = {
        'course':course,
    }
    return render(request,'checkout.html',context=context)
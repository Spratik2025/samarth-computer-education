from django.shortcuts import render
from .models import StudentRegistration

def home(request):
    if request.method == "POST":
        StudentRegistration.objects.create(
            name=request.POST.get("name"),
            mobile=request.POST.get("mobile"),
            email=request.POST.get("email"),
            course=request.POST.get("course")
        )

    return render(request, 'home.html')
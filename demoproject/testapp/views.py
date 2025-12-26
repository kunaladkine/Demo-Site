from django.shortcuts import render

from django.contrib import messages

# Create your views here.

def home(request):
  return render(request, "home.html")

def aboutus(request):
  return render(request,"aboutus.html")

def contactus(request):
  return render(request, "contactus.html")

def services(request):
  return render(request, "services.html")

def login(request):
  return render(request, "login.html")

from django.contrib import messages

def enroll(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        course = request.POST.get("course")

        # Later we can save to DB (if needed)
        print(name, email, phone, course)  # For now displaying in console

        messages.success(request, f"Thank you {name}! You successfully enrolled for {course}. 🎉")
        return render(request, "enroll.html")

    return render(request, "enroll.html")
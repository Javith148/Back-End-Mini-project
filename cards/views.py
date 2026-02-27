from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import addImage,SendOtp
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
import random
from django.conf import settings
import random
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import SendOtp

def home(request):

    posts = addImage.objects.all()
    paginator=Paginator(posts, 4)
    page_number =request.GET.get("page")
    posts = paginator.get_page(page_number)
     
    return render(request, 'show.html', {'posts': posts})

def upload(request):
    if request.method == "POST":
        title = request.POST.get('title')
        image = request.FILES.get('image')
        des =request.POST.get('des')

        if title and image:
            addImage.objects.create(title=title, image=image, des=des)
            return redirect('show')  

    return render(request, "upload.html")


def viewDetail(request, id):
    btn= get_object_or_404 (addImage,id=id)
    return render(request, 'viewall.html',{'post': btn})




def emailotp(request):

    email = 'mownika18.m@gmail.com'
    otp = str(random.randint(100000, 999999))

    # Save OTP in DB
    SendOtp.objects.create(email=email, otp=otp)

    # Send Email
    send_mail(
        subject="OTP SENT",
        message=f"Your OTP is {otp}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )

    return JsonResponse({
        'email': email,
        'otp': otp,
        'message': "OTP sent successfully"
    })





from django.conf import settings
from django.shortcuts import render
from .models import *
from django.http import JsonResponse

def test_page(request):
    return render(request, 'test.html')

def main_page(request):
    sevices=Services.objects.all().order_by('index')
    company=Company.objects.first()
    links=SocialLinks.objects.all()
    sliders=Slider.objects.all().order_by('index')
    context={
        "services":sevices,
        "company":company,
        "links":links,
        "sliders":sliders
    }
    return render(request, 'index.html', context)


from django.core.mail import send_mail
def contactUs(request):
    if request.method == 'POST':
        print(request.POST)
        fullname = request.POST['fullname']
        email = request.POST['email']
        subject = request.POST['subject']
        client_message = request.POST['message']
        phone = request.POST['phone']
        print(phone)
        if(fullname=="" or email=="" or subject=="" or client_message==""):
            context={
                "result":'error',
                "msg":"Please fill all fields!!"
            }
        else:
            contact_us=ContactUs.objects.create(
                name=fullname,
                email=email,
                subject=subject,
                message=client_message,
                phone=phone
            )
            html_message=f"""
                <h3>Dear Mr.Mustafa Hassan,</h3>
                You have a new message from {fullname} having the email: {email}<br>
                message subject:{subject} <br>
                Message content:{client_message}<br>
                <a style="color:#83B641" href="https://www.proventus-solutions.com/admin/main/contactus/{contact_us.pk}/change/" >Click here</a> for more details
            """
            send_mail(
                f"Message from {fullname}",  # Subject of the email
                html_message,  # Message of the email
                settings.EMAIL_HOST_USER,  # Sender's email address
                [settings.EMAIL_RECEIVER],  # List of recipient(s)
                fail_silently=False,  # Set to True to suppress exceptions
                html_message=html_message
            )

            context={
                "result":'success',
                "msg":"message sent"
            }
        return JsonResponse(context)
 

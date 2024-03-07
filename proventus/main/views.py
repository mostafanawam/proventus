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
    sliders=Slider.objects.all()
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
        fullname = request.POST['fullname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        if(fullname=="" or email=="" or subject=="" or message==""):
            context={
                "result":'error',
                "msg":"Please fill all fields!!"
            }
        else:
            send_mail(
                subject,  # Subject of the email
                message,  # Message of the email
                settings.EMAIL_HOST_USER,  # Sender's email address
                [settings.EMAIL_HOST_USER],  # List of recipient(s)
                fail_silently=False,  # Set to True to suppress exceptions
            )
            contact_us=ContactUs.objects.create(
                name=fullname,
                email=email,
                subject=subject,
                message=message
            )
        # try:
        #     settings=Settings.objects.get()
        #     html_message=f"""
        #         <h3>Hello Dear, <br> 
        #         You have a new message from {fullname} having the email: {email}<br>
        #         message subject:{subject} <br>
        #         Message content:{message}<br>
        #         <a style="color:#83B641" href="{settings.admin_link}/home/contactus/{contact_us.pk}/change/" >Click here</a> for more details
        #         </h3>
        #     """
        #     send_email(f"New Message from {fullname}",html_message,settings.reciever_email)
        # except Exception as e:
        #     print(f"email didnt send,{e}")

            context={
                "result":'success',
                "msg":"message sent"

            }
        return JsonResponse(context)
 

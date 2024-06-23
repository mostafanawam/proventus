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
             <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 20px;">
    <div style="background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
        <div style="background-color: #39b54a; color: #ffffff; padding: 10px; border-radius: 8px 8px 0 0; text-align: center;">
            <h3 style="margin: 0;">New Message Notification</h3>
        </div>
        <div style="margin-top: 20px;">
            <p>Dear Mr. Mustafa Hassan,</p>
            <p>You have a new message from <strong>{fullname}</strong> having the email: <strong>{email}</strong>.</p>
            <p><strong>Message Subject:</strong> {subject}</p>
            <p><strong>Message Content:</strong></p>
            <p>{client_message}</p>
            <p style="text-align: center;">
                <a href="https://www.proventus-solutions.com/admin/main/contactus/{contact_us.pk}/change/" 
                   style="display: inline-block; background-color: #39b54a; color: #ffffff; padding: 10px 20px; text-decoration: none; border-radius: 5px; margin-top: 20px;">
                   Click here for more details
                </a>
            </p>
        </div>
        <div style="margin-top: 20px; font-size: 12px; color: #888888; text-align: center;">
            <p>This is an automated message. Please do not reply directly to this email.</p>
        </div>
    </div>
</body>
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
 

from django.shortcuts import render 
from django.core.mail import send_mail
from django.contrib import messages
from django.http import JsonResponse
from .models import Contact
from django.conf import settings
from django.core.mail import send_mail
import smtplib
from email.message import EmailMessage

# Create your views here.
def home(request):
    responce_data = {}
    # save data using ajax
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        responce_data['name'] = name
        responce_data['email'] = email
        responce_data['subject'] = subject
        responce_data['message'] = message
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()        
    return render(request, 'Dashboard.html',)


# sender_email = 'support@gautamankul.me'
# receiver_email = "dhanushg0543@gmail.com"
# smtp_server = 'mail.privateemail.com'
# login = "support@gautamankul.me"
# password = "Jobs@8546"
# port = 465

# def send_email(request):
#     message = EmailMessage()
#     message["Subject"] = "Your Subject"
#     message["From"] = f"Your Display Name <{sender_email}>"
#     message["To"] = receiver_email
#     content = "Hello world"
#     message.set_content(content)
#     server = smtplib.SMTP_SSL(smtp_server, port)
#     server.login(login, password)
#     server.send_message(message)
#     server.quit()
#     return JsonResponse({'message': 'Email sent successfully'})
    


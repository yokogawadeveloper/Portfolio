from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contact
from email.message import EmailMessage
import smtplib


# Email Settings for namecheap
sender_email = 'support@gautamankul.me'
smtp_server = 'mail.privateemail.com'
login = "support@gautamankul.me"
password = "Jobs@8546"
port = 465


@receiver(post_save, sender=Contact)
def send_email(sender, instance, created, **kwargs):
    if created:
        message = EmailMessage()
        message["Subject"] = instance.subject
        message["From"] = f"Gautam Ankul<{sender_email}>"
        message["To"] = [sender_email]
        content = "Greetings from Gautam Ankul, \n\n" + instance.message + \
            "\n\n" + "Name: " + instance.name + "\n" + "Email: " + instance.email
        message.set_content(content)
        server = smtplib.SMTP_SSL(smtp_server, port)
        server.login(login, password)
        server.send_message(message)
        server.quit()
        # send mail to user
        message = EmailMessage()
        message["Subject"] = "Thank you for contacting us"
        message["From"] = f"Gautam Ankul<{sender_email}>"
        message["To"] = [instance.email]
        content = "Thank you for contacting us. We will get back to you soon."
        message.set_content(content)
        server = smtplib.SMTP_SSL(smtp_server, port)
        server.login(login, password)
        server.send_message(message)
        server.quit()

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings


@receiver(pre_save, sender=Contact)
def send_email(sender, instance, **kwargs):
    subject = "Thank you for contacting us"
    message = "Thank you for contacting us. We will get back to you soon."
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [instance.email]
    send_mail(subject, message, email_from, recipient_list, fail_silently=True)

    # send mail to admin
    subject = instance.subject
    message = "Greetings from Gautam Ankul, \n\n" + instance.message + \
        "\n\n" + "Name: " + instance.name + "\n" + "Email: " + instance.email
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_HOST_USER]
    send_mail(subject, message, email_from, recipient_list, fail_silently=True)

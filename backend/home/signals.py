
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import UserContact

@receiver(post_save, sender=UserContact)
def send_contact_confirmation(sender, instance, created, **kwargs):
    if created:  
        subject = f"Thank you for contacting us, {instance.name}"
        message = f"""
        Hello {instance.name},

        Thank you for your interest in our courses. Here are your contact details:
        Name: {instance.name}
        Email: {instance.email}
        Contact: {instance.contact}
        Course: {instance.course}
        Preferred Mode: {instance.cmode}

        We will get back to you soon.
        """
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]  

      
        send_mail(subject, message, from_email, recipient_list)

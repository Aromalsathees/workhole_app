from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_registration_email(email):
    subject = "Registration Successful"
    message = "You have successfully registered."
    from_email = "youremail@example.com"  # Update with your email
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
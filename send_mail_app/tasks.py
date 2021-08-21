from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from celery_practice import settings
User = get_user_model()

@shared_task(bind=True)
def send_mail_func(self):
    users = User.objects.all()
    for user in users:
        mail_subject = "Celery testing"
        message = "Message text"
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True
        )
    return "Done"

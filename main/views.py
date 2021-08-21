from django.shortcuts import render
from django.http import HttpResponse
from .tasks import test_func
from send_mail_app.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json


def test(request):
    test_func.delay()
    return HttpResponse("Done")


def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Send")


# for dynamic task
def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=22,
                                                              minute=10,
                                                              day_of_month=16,
                                                              month_of_year=8)
    task = PeriodicTask.objects.create(crontab=schedule,
                                       name="schedule_mail_task_" + "2",
                                       task="send_mail_app.tasks.send_mail_func")#, args=json.dumps(([2, 3])))
    return HttpResponse("Done")

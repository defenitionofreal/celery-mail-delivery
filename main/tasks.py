# Create your tasks here
from celery import shared_task
from celery_practice.celery import app



@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return "Done"



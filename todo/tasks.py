from celery import Celery, shared_task

app = Celery('todo', broker='redis://localhost:6379/')


@shared_task
def hello_world(self):
    print('Hello world!, Congratulation this one is working ')

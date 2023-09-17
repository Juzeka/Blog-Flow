from django.core.mail import send_mail
from core.celery import app
from django.conf import settings


def trigger_task(task, *args, **kwargs):
    if settings.USE_CELERY:
        task.apply_async(*args, **kwargs)
    else:
        return task(*args, **kwargs)

@app.task
def notify_email(**kwargs):
    subject = kwargs.get('subject')
    message = kwargs.get('message')
    from_email = kwargs.get('from_email')
    recipient_list = kwargs.get('recipient_list')

    send_mail(subject, message, from_email, recipient_list)

    return {'detail': 'E-mail enviado com sucesso.', 'data': kwargs}

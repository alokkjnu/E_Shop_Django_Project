from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    """
    task to send an email notification when an order is successfully placed
    :param order_id:
    :return:
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order_id)
    message = 'Dear {},\n\nYou have successfully placed an order. \ ' \
              'Your order id is {}.'.format(order.first_name, order_id)
    mail_sent = send_mail(subject, message, 'alokk9490@gmail.com', [order.email])
    return mail_sent

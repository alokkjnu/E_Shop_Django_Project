from django.apps import AppConfig


class PaymentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'payment'
   # verbose_name = 'payment'

   # def ready(self):
        #import signal handlers
        #import payment.signals
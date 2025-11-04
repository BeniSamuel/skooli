from django.db import models

# Create your models here.
class Notification(models.Model):
    content = models.CharField()
    sent_at = models.DateTimeField()
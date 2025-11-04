from django.db import models

# Create your models here.
class Discipline(models.Model):
    mistake = models.CharField()
    occured_at = models.DateTimeField()
    deducted_marks = models.IntegerField()

    class Meta:
        pass


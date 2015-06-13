import datetime

from django.db import models
from django.utils import timezone


class Source(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


GENDER_CHOICES = (
    ('F', 'Female'),
    ('M', 'Male'),
)


class Patient(models.Model):
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, null=True, blank=True, editable=False)
    source = models.ForeignKey(Source)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, null=True, blank=True, choices=GENDER_CHOICES)
    tour_date = models.DateField(default=timezone.now)
    new_patient = models.BooleanField(default=True)

    @property
    def age(self):
        if self.birth_date:
            bday = self.birth_date
            d = datetime.date.today()
            return (d.year - bday.year) - int((d.month, d.day) < (bday.month, bday.day))
        else:
            return None

    def __unicode__(self):
        return self.fullname


class HappyBirthdayPatient(models.Model):
    fullname = models.CharField(max_length=50)
    birth_date = models.DateField()
    address = models.CharField(max_length=120)

    @property
    def birth_date_month(self):
        return self.birth_date.strftime('%B')

    @property
    def age(self):
        if self.birth_date:
            bday = self.birth_date
            d = datetime.date.today()
            return (d.year - bday.year) - int((d.month, d.day) < (bday.month, bday.day))
        else:
            return None

    def __unicode__(self):
        return self.fullname
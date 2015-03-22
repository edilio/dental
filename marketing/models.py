from django.db import models
from django.utils import timezone
from django.conf import settings


class Vehicle(models.Model):
    name = models.CharField(max_length=70)

    def __unicode__(self):
        return self.name


def guess_year():
    now = timezone.now()
    year = now.year
    if now.month < 4:
        return year - 1
    else:
        return year


class Flight(models.Model):
    number = models.PositiveIntegerField(default=1)
    year = models.PositiveSmallIntegerField(default=guess_year)
    first_day = models.DateField()
    last_day = models.DateField()

    def save(self, *args, **kwargs):
        self.year = self.first_day.year
        super(Flight, self).save(*args, **kwargs)

    def __unicode__(self):
        return "{}-{}-{}".format(self.year, self.first_day, self.last_day)


class SpotTime(models.Model):
    vehicle = models.ForeignKey(Vehicle)
    scheduled = models.DateTimeField(null=True, blank=True)
    air_time = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return "{} Scheduled: {} AirTime: {}".format(self.vehicle.name, self.scheduled, self.air_time)


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name


GENDER_CHOICES = (
    ('F', 'Female'),
    ('M', 'Male'),
)


class Lead(models.Model):
    phone_number = models.CharField(max_length=15)
    vehicle = models.ForeignKey(Vehicle)
    name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, null=True, blank=True, choices=GENDER_CHOICES)
    category = models.ForeignKey(Category)
    comments = models.TextField(null=True, blank=True)
    lm = models.BooleanField(help_text='Left Message', default=False)
    appointment_date = models.DateTimeField(null=True, blank=True)

    email = models.EmailField(null=True, blank=True)
    entered_date = models.DateField(default=timezone.now)
    entered_by = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)

    @property
    def short_comments(self):
        if len(self.comments) > 17:
            return self.comments[:17] + '...'
        else:
            return self.comments

    @property
    def age(self):
        if self.birth_date:
            bday = self.birth_date
            d = timezone.datetime.today()
            return (d.year - bday.year) - int((d.month, d.day) < (bday.month, bday.day))
        else:
            return None

    def __unicode__(self):
        return '{} phone: {}'.format(self.name, self.phone_number)
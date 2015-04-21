from django.apps import apps
from django.db import models
from django.utils import timezone
from django.conf import settings


def get_model(app, model_name):
    return apps.get_app_config(app).get_model(model_name)


class AdType(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Vehicle(models.Model):
    name = models.CharField(max_length=70)
    ad_type = models.ForeignKey(AdType, default=1)

    def __unicode__(self):
        return self.name


def guess_year():
    now = timezone.now()
    year = now.year
    if now.month < 4:
        return year - 1
    else:
        return year


def next_index(model_name, app='marketing'):
    result = 0
    try:
        model = get_model(app, model_name)

        qs = model.objects
        m = qs.reverse()[0]
        result = m.number
    except IndexError:
        pass
    return result + 1


def next_flight():
    return next_index('Flight')


class Flight(models.Model):
    number = models.PositiveIntegerField(default=next_flight)
    year = models.PositiveSmallIntegerField(default=guess_year)
    first_day = models.DateField()
    last_day = models.DateField()

    def save(self, *args, **kwargs):
        self.year = self.last_day.year
        super(Flight, self).save(*args, **kwargs)

    def __unicode__(self):
        return "{} => {}".format(self.first_day, self.last_day)


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


class DentalOffice(models.Model):
    name = models.CharField(max_length=20)

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
    office = models.ForeignKey(DentalOffice, null=True, blank=True)

    email = models.EmailField(null=True, blank=True)

    flight = models.ForeignKey(Flight, default=True, blank=True)

    entered_date = models.DateField(default=timezone.now)
    entered_by = models.ForeignKey(settings.AUTH_USER_MODEL)

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

    def get_ad_type(self):
        return self.vehicle.ad_type.id

    def __unicode__(self):
        return '{} phone: {}'.format(self.name, self.phone_number)

    def save(self, *args, **kwargs):
        now = timezone.now()
        flights = Flight.objects.filter(first_day__lte=now, last_day__gte=now)
        if flights:
            self.flight = flights[0]
        super(Lead, self).save(*args, **kwargs)

from datetime import date, timedelta

from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from .models import Source, Patient, HappyBirthdayPatient

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('new_patient', 'fullname', 'source', 'tour_date', 'gender', 'age', 'birth_date')
    list_display_links = ('new_patient', 'fullname',)
    search_fields = ('fullname', 'phone')
    list_filter = ('gender', 'source', 'tour_date', 'new_patient')


class MonthBornListFilter(SimpleListFilter):
    title = _('birthday month')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'birth_date_month'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            (1, _('in January')),
            (2, _('in February')),
            (3, _('in March')),
            (4, _('in April')),
            (5, _('in May')),
            (6, _('in June')),
            (7, _('in July')),
            (8, _('in August')),
            (9, _('in September')),
            (10, _('in October')),
            (11, _('in November')),
            (12, _('in December')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        value = self.value()
        if value:
            return queryset.filter(birth_date__month=value)


class AgeListFilter(SimpleListFilter):
    title = _('age')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'age'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('infant', _('infant')),
            ('toddler', _('toddler')),
            ('kid', _('kid')),
            ('teenager', _('teenager')),
            ('young adult', _('young adult')),
            ('adult', _('adult')),
            ('middle aged', _('middle aged')),
            ('senior citizens', _('senior citizens')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        value = self.value()
        days_per_year = 365.24
        now = timezone.now()
        if value == 'infant':
            from_date = now + timedelta(-1*days_per_year)
            return queryset.filter(birth_date__gt=from_date)
        if value == 'toddler':
            from_date = now + timedelta(-2*days_per_year)
            to_date = now + timedelta(-1*days_per_year)
            return queryset.filter(birth_date__gt=from_date, birth_date__lt=to_date)
        if value == 'kid':
            from_date = now + timedelta(-12*days_per_year)
            to_date = now + timedelta(-2*days_per_year)
            return queryset.filter(birth_date__gt=from_date, birth_date__lt=to_date)
        if value == 'teenager':
            from_date = now + timedelta(-19*days_per_year)
            to_date = now + timedelta(-12*days_per_year)
            return queryset.filter(birth_date__gt=from_date, birth_date__lt=to_date)
        if value == 'young adult':
            from_date = now + timedelta(-25*days_per_year)
            to_date = now + timedelta(-19*days_per_year)
            return queryset.filter(birth_date__gt=from_date, birth_date__lt=to_date)
        if value == 'adult':
            from_date = now + timedelta(-40*days_per_year)
            to_date = now + timedelta(-25*days_per_year)
            return queryset.filter(birth_date__gt=from_date, birth_date__lt=to_date)
        if value == 'middle aged':
            from_date = now + timedelta(-62*days_per_year)
            to_date = now + timedelta(-40*days_per_year)
            return queryset.filter(birth_date__gt=from_date, birth_date__lt=to_date)
        if value == 'senior citizens':
            to_date = now + timedelta(-62*days_per_year)
            return queryset.filter(birth_date__lt=to_date)

# infant (< 1 year)
# toddler (between 1 to 2 years)
# kid (before puberty)
# teenager (after puberty but < 19 years)
# young adult (between 19 to 25 years)
# simply called adult??
# middle aged person( 40-62)
# senior citizens > 62

@admin.register(HappyBirthdayPatient)
class HappyBirthdayPatientAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'address', 'birth_date', 'birth_date_month', 'age', 'treatment')
    list_filter = (MonthBornListFilter, AgeListFilter, 'treatment')
    search_fields = ('fullname', 'address')
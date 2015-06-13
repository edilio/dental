from datetime import date

from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.utils.translation import ugettext_lazy as _

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


@admin.register(HappyBirthdayPatient)
class HappyBirthdayPatientAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'address', 'birth_date', 'birth_date_month', 'age')
    list_filter = (MonthBornListFilter, )
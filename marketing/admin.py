
from django.contrib import admin
from .models import Vehicle, Flight, Category, SpotTime, Lead, DentalOffice

from spot_times import guess_vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(DentalOffice)
class DentalOfficeAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('year', 'first_day', 'last_day')

    readonly_fields = ('year', )
    list_filter = ('year', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(SpotTime)
class SpotTimeAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'scheduled', 'air_time')
    list_filter = ('vehicle', 'scheduled', 'air_time')


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'phone_number', 'name', 'birth_date', 'age', 'gender', 'category', 'lm',
                    'appointment_date', 'office',
                    'entered_date', 'entered_by', 'short_comments', 'email')

    list_filter = ('vehicle', 'lm', 'gender', 'category', 'appointment_date', 'office', 'entered_by')
    search_fields = ('phone_number', 'name', 'email')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'entered_by', None) is None:
            obj.entered_by = request.user
        obj.save()

    def get_form(self, request, obj=None, **kwargs):
        form = super(LeadAdmin, self).get_form(request, obj, **kwargs)
        vehicle = guess_vehicle()
        if vehicle:
            form.base_fields['vehicle'].initial = vehicle
        return form
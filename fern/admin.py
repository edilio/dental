from django.contrib import admin

from .models import Source, Patient

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('new_patient', 'fullname', 'source', 'tour_date', 'gender', 'age', 'birth_date')
    list_display_links = ('new_patient', 'fullname',)
    search_fields = ('fullname', 'phone')
    list_filter = ('gender', 'source', 'tour_date', 'new_patient')
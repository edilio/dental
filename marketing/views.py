from django.shortcuts import render
from django.utils import timezone

from rest_framework import viewsets, filters, generics
from rest_framework.response import Response

from .models import *
from .serializers import LeadSerializer, CallSerializer


def calls_per_flight(request):
    now = timezone.now()
    context = {
        'years': Flight.objects.values('year').distinct(),
        'flights': Flight.objects.all(),
        'ad_types': AdType.objects.all(),
        'default_year': now.year
    }
    return render(request, 'marketing/calls-per-flight.html', context=context)


class LeadViewSet(viewsets.ModelViewSet):
    model = Lead
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('phone_number', 'flight')

    def get_queryset(self):
        qs = super(LeadViewSet, self).get_queryset()
        ad_type = self.request.QUERY_PARAMS.get('ad_type')
        if ad_type is not None:
            qs = qs.filter(vehicle__ad_type=ad_type)
        return qs


class CallListView(generics.ListAPIView):
    queryset = Lead.objects.all()
    serializer_class = CallSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('phone_number', 'flight')

    def get_queryset(self):
        qs = super(CallListView, self).get_queryset()
        ad_type = self.request.QUERY_PARAMS.get('ad_type')
        if ad_type is not None:
            qs = qs.filter(vehicle__ad_type=ad_type)
        return qs

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        summary = {}
        for lead in queryset:
            if lead.entered_date in summary:
                entered_date_summary = summary[lead.entered_date]
                entered_date_summary["count"] += 1
            else:
                summary[lead.entered_date] = {
                    "entered_date": lead.entered_date,
                    "count": 1
                }
        data = [summary[key] for key in summary.keys()]
        data = sorted(data, key=lambda call: call["entered_date"])
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)
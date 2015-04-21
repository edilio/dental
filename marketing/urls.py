
from django.conf.urls import patterns, url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'leads', views.LeadViewSet)

urlpatterns = patterns('marketing.views',
    url(r'^api/', include(router.urls)),
    url(r'^api/calls/$', views.CallListView.as_view()),
    url(r'^calls-per-flight', views.calls_per_flight, name='calls_per_flight'),

)
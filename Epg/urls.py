from django.conf.urls import url
from soapserver.views import epg_soap_service

urlpatterns = [
    url(r'^api/epg/', epg_soap_service),
]

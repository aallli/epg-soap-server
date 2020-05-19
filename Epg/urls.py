from django.conf.urls import url
from spyne.server.django import DjangoView
from soapserver.views import hello_world_service, app, HelloWorldService
from spyne.protocol.soap import Soap11

urlpatterns = [
    url(r'^api1/', hello_world_service),
    url(r'^api2/', DjangoView.as_view(
        services=[HelloWorldService], tns='soapserver',
        in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())),
    url(r'^api3/', DjangoView.as_view(
        services=[HelloWorldService], tns='soapserver',
        in_protocol=Soap11(validator='lxml'), out_protocol=Soap11(),
        cache_wsdl=False)),
    url(r'^api/', DjangoView.as_view(application=app)),
]

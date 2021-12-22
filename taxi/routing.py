from django.core.asgi import get_asgi_application
from django.urls import path # new

from channels.routing import ProtocolTypeRouter, URLRouter # changed

from taxi.middleware import TokenAuthMiddlewareStack
from trips.consumers import TaxiConsumer

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    # new
    'websocket': TokenAuthMiddlewareStack(
        URLRouter([
            path('taxi/', TaxiConsumer.as_asgi()),
        ])
    ),
})
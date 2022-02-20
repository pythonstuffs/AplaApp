from django.conf.urls import url

from channels.routing import ChannelNameRouter, ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from ecommorce.consumers import ecommorce_WebSocketConsumer

# Consumer Imports
from Country_State_List.consumers import Country_State_ListConsumer
from users.consumers import usersConsumer
from BusinessOwener.consumers import BusinessOwenerConsumer


application = ProtocolTypeRouter({

    # WebSocket handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r"^ws/$", ecommorce_WebSocketConsumer.as_asgi()),
        ])
    ),
    "channel": ChannelNameRouter({
        "Country_State_List": Country_State_ListConsumer,    "users": usersConsumer,    "BusinessOwener": BusinessOwenerConsumer,
    })
})

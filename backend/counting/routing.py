from django.urls import path, re_path
from .consumer import WSComsumer
from channels.routing import URLRouter, ProtocolTypeRouter

ws_urlpatterns = [
    re_path(r'ws/test/', WSComsumer.as_asgi())
]


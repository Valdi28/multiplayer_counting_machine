from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import async_to_sync, sync_to_async
from channels.db import database_sync_to_async
from .models import Seasons
from .serializers import SeasonsSerializer

class WSComsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.group = 'counting'
        await self.accept()
        await self.channel_layer.group_add(
            self.group,
            self.channel_name
        )

        await self.update_count(None)


    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data = json.loads(text_data)
        # message = 
        request_type = dict.get(text_data, 'type', None)
        if request_type == 'update_count':
            await self.channel_layer.group_send(
                self.group,
                {
                    'type': 'update_count',
                    'payload': 'xd'
                }
            )
        elif request_type == 'add_count':
            await self.set_last_season_count()
        
    
    async def update_count(self, event):
        last_season = await self.get_last_season()
        await self.send(
            json.dumps({
                'type': 'update_count',
                'count': last_season.count
                })
        )

    @database_sync_to_async
    def get_last_season(self):
        last_season = Seasons.objects.all().order_by('-creation_date').first()

        return last_season

    @database_sync_to_async
    def set_last_season_count(self, count=0):
        last_season = Seasons.objects.order_by('-creation_date').first()
        last_season_serializer = SeasonsSerializer(last_season, {
            'season_number': last_season.season_number,
            'count': last_season.count + 1
        })
        # last_season_serializer.data = {
        #     'season_number': dict.get(last_season_serializer.initial_data, 'season_number', last_season.season_number),
        #     'count': dict.get(last_season_serializer.initial_data, 'count', None) + 1
        # }

        if last_season_serializer.is_valid():
            last_season_serializer.save()
        else:
            raise last_season_serializer.errors

    
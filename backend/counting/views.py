from django.shortcuts import render
from django.http import Http404 
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .models import Seasons
from .serializers import SeasonsSerializer
# from .serializers import CountSerializer, CustomUSerSerializer
# from .models import Count

# Create your views here.
# class CountView(viewsets.ModelViewSet):
#     serializer_class = CountSerializer
#     queryset = Count.objects.all()


# class CustomUserView(viewsets.ModelViewSet):
#     serializer_class  = CustomUSerSerializer
#     queryset = Count.objects.all()


class SeasonsView(APIView):
    def get(self, request):
        
        seasons = Seasons.objects.all().order_by('-creation_date')

        serializer = SeasonsSerializer(seasons, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        seasons = Seasons.objects.all().order_by('-creation_date')

        

        if "season_number" in request.data:
            season_number = request.data["season_number"]
        else:
            all_items_serializer = SeasonsSerializer(seasons, many=True)
            try:
                season_number = all_items_serializer.data[0]["season_number"] + 1
            except:
                season_number = 1
        #season_number = seasons[0]["season_number"] + 1
        # except:
        #     season_number = 1
        data = {
            "season_number": season_number
        }
        serializer = SeasonsSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SeasonView(APIView):
    def get(self, request, season_number):
        try:
            if not season_number:
                seasons = Seasons.objects.all()

                serializer = SeasonsSerializer(season)

                return Response(serializer.data, status=status.HTTP_200_OK)
            
            season = Seasons.objects.get(season_number=season_number)

            serializer = SeasonsSerializer(season)
            return Response(serializer.data)
        except:
            raise Http404

    def delete(self, request, season_number):
        try:
            season = Seasons.objects.get(season_number=season_number)
            serializer = SeasonsSerializer(season, many=False)

            season.delete()

            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        except:
            raise Http404

    def put(self, request, season_number):
        season = Seasons.objects.get(season_number=season_number)
        if not "season_number" in request.data:
            request.data["season_number"] = season.season_number
        serializer = SeasonsSerializer(season, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class SeasonCountView(APIView):
    def put(self, request, season_number):
        
            try:
                default_quantity = 1


                season = Seasons.objects.get(season_number=season_number)


                serializer = SeasonsSerializer(season, data=request.data)
                
                if not "season_number" in request.data:
                    request.data["season_number"] = season.season_number

                if not "quantity" in request.data:
                    request.data['count'] = season.count + default_quantity
                else:
                    try:
                        if not season.count + request.data['quantity'] < 0:
                            request.data['count'] = season.count + request.data['quantity']
                        else:
                            request.data['count'] = 0
                    except:
                        return Response({
                            'quantity': "Enter valid data"
                        }, status.HTTP_400_BAD_REQUEST)
                    

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status.HTTP_200_OK)
            
                return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
            except:
                raise Http404

    def delete(self, request, season_number):
        try:
            season = Seasons.objects.get(season_number=season_number)

            data = {
                "season_number": season.season_number,
                "count": 0
            }

            serializer = SeasonsSerializer(season, data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_204_NO_CONTENT)
            return Response(serializer.errors, status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            raise Http404

class LatestSeasonView(APIView):
    def get(self, request):
        
        try:
            latest_season = Seasons.objects.order_by('-season_number').all().first()

            serializer = SeasonsSerializer(latest_season)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except:
            raise Http404

    def delete(self, request):
        try:
            latest_season = Seasons.objects.order_by('-season_number').all().first()

            serializer = SeasonsSerializer(latest_season)
            latest_season.delete()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        
        except:
            raise Http404
        
    def put(self, request):
        try:
            latest_season = Seasons.objects.all().order_by("-season_number").first()

            serializer = SeasonsSerializer(latest_season, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_200_OK)
            
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        except:
            raise Http404

class LatestSeasonCountView(APIView):
    def put(self, request):
        try:
            default_quantity = 1


            season = Seasons.objects.all().order_by('-season_number').first()


            serializer = SeasonsSerializer(season, data=request.data)
            
            if not "season_number" in request.data:
                request.data["season_number"] = season.season_number

            if not "quantity" in request.data:
                request.data['count'] = season.count + default_quantity
            else:
                try:
                    if not season.count + request.data['quantity'] < 0:
                        request.data['count'] = season.count + request.data['quantity']
                    else:
                        request.data['count'] = 0
                except:
                    return Response({
                        'quantity': "Enter valid data"
                    }, status.HTTP_400_BAD_REQUEST)                    

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_200_OK)
        
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        except:
            raise Http404
        
    def delete(self, request):
        try:
            season = Seasons.objects.all().order_by('-season_number').first()

            data = {
                "season_number": season.season_number,
                "count": 0
            }

            serializer = SeasonsSerializer(season, data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_204_NO_CONTENT)
            return Response(serializer.errors, status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            raise Http404
        
class TestHome(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {
            "Welcome! You are logged!"
        }
        return Response(content)
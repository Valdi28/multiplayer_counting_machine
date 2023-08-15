from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework import status

# Create your views here.
class Logout(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):

        refresh_token = RefreshToken(dict.get(request.data, "refresh"))
        refresh_token.blacklist()

        return Response(status=status.HTTP_205_RESET_CONTENT)
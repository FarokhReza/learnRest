from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import UserRegisterSerializer, UserSeializer
# Create your views here.


class UserRegister(APIView):
    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.POST) # we send info
        # as data instated of instance until we be able to check it
        if ser_data.is_valid():
            User.objects.create_user(
                username = ser_data.validated_data['username'],
                email = ser_data.validated_data['email'],
                password = ser_data.validated_data['password'],
            )
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserViewSet(viewsets.ViewSet): # if task is simple we use viewset, for complexe task we use 
    # apiview (((object custome permission dosenot work for this state)))

    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def list(self, request):
        srz_data = UserSeializer(instance=self.queryset, many=True)
        return Response(data=srz_data.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        srz_data = UserSeializer(instance=user)
        return Response(data=srz_data.data)

    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)

        if user != request.user:
            return Response({'permission denied' : 'your not the owner'})

        srz_data = UserSeializer(instance=user, data=request.POST, partial=True)
        
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data)
        return RecursionError(data=srz_data.errors)

    def destroy(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)

        if user != request.user:
            return Response({'permission denied' : 'your not the owner'})

        user.is_active = False
        user.save()

        return Response({'message': 'user deactiveted!'}) 
    

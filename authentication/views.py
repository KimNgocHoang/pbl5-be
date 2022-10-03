from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework import viewsets
from .models import User
from pot.models import Plant
from .serializers import UserCreationSerializer
from pot.serializers import PlantSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class HelloAuthView(generics.GenericAPIView):

    def get(self,request):
        return Response(data={"mess":"hello"},status=status.HTTP_200_OK)


class UserCreateView(generics.GenericAPIView):
    serializer_class = UserCreationSerializer
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer
    permission_class = [IsAdminUser]


    @action(detail=False, methods=['post'])
    def add_user(self, request ):
        serializer = UserCreationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True, methods=['get'])
    def get_plant(self, request, pk):
        customer = self.get_object()
        if customer:
            plants = Plant.objects.filter(customer=customer)
            if plants.exists():
                rs = PlantSerializer(plants, many=True)
                return Response(rs.data, status=status.HTTP_200_OK)
            else:
                return Response({"error_message": "plant is not defined! "}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error_message": "user is not defined!"}, status=status.HTTP_400_BAD_REQUEST)
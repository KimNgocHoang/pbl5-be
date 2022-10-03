from rest_framework import status
from rest_framework.decorators import action
from .models import Plant, History_Pest, History_Water
from .serializers import PlantSerializer, HistoryPestSerializer, HistoryWaterSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAdminUser


class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    # permission_classes = [IsAuthenticated]   

    permission_map = {
        "list": [IsAdminUser],
        "add_plant": [IsAuthenticated]
    } 

    @action(detail=True, methods=['get'])
    def get_plant(self, request, pk):
        plant = self.get_object()
        if plant:
            serializer = PlantSerializer(plant)
            return Response(serializer.data, status=status.HTTP_200_OK)    
        return Response({"error_message": "plant id is not defined!"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def add_plant(self, request ):
        serializer = PlantSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'])
    def update_plant(request, self, pk):
        plant = self.get_object()
        if plant:
            serializer = PlantSerializer(plant, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error_message": "plant id is not defined!"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'])
    def delete_plant(self, request, pk):
        plant = self.get_object()
        if plant:
            plant.delete()
            return Response({"details": "Completed delete plant!"}, status=status.HTTP_200_OK)
        return Response({"error_message": "plant id is not defined!"}, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True, methods=['get'])
    def get_history_pest(self, request, pk):
        plant = self.get_object()
        if plant:
            history_pest = History_Pest.objects.filter(plant=plant)
            if history_pest.exists():
                rs = HistoryPestSerializer(history_pest, many=True)
                return Response(rs.data, status=status.HTTP_200_OK)
            else:
                return Response({"error_message": "history_pest is not defined! "}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error_message": "plant is not defined!"}, status=status.HTTP_400_BAD_REQUEST)

 
    @action(detail=True, methods=['get'])
    def get_history_water(self, request, pk):
        plant = self.get_object()
        if plant:
            history_water = History_Water.objects.filter(plant=plant)
            if history_water.exists():
                rs = HistoryWaterSerializer(history_water, many=True)
                return Response(rs.data, status=status.HTTP_200_OK)
            else:
                return Response({"error_message": "history_water is not defined! "}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error_message": "plant is not defined!"}, status=status.HTTP_400_BAD_REQUEST)


class HistoryPestViewSet(viewsets.ModelViewSet):
    queryset = History_Pest.objects.all()
    serializer_class = HistoryPestSerializer
    # permission_classes = [IsAuthenticated]   


    @action(detail=False, methods=['post'])
    def add_history_pest(self, request):
        serializer = HistoryPestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    @action(detail=False, methods=['put'])
    def update_history_pest(self, request, pk):
        history_pest = self.get_object()
        if history_pest:
            serializer = HistoryPestSerializer(history_pest, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error_message": "history_pest id is not defined!"}, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True, methods=['delete'])
    def delete_history_pest(self, request, pk):
        history_pest = self.get_object()
        if history_pest:
            history_pest.delete()
            return Response({"details": "Completed delete history_pest!"}, status=status.HTTP_200_OK)
        return Response({"error_message": "history_pest id is not defined!"}, status=status.HTTP_400_BAD_REQUEST)
    

class HistoryWaterViewSet(viewsets.ModelViewSet):
    queryset = History_Water.objects.all()
    serializer_class = HistoryWaterSerializer
    # permission_classes = [IsAuthenticated]   


    @action(detail=False, methods=['post'])
    def add_history_water(self, request):
        serializer = HistoryWaterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    @action(detail=False, methods=['put'])
    def update_history_water(self, request, pk):
        history_water = self.get_object()
        if history_water:
            serializer = HistoryWaterSerializer(history_water, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error_message": "history_water id is not defined!"}, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True, methods=['delete'])
    def delete_history_water(self, request, pk):
        history_water = self.get_object()
        if history_water:
            history_water.delete()
            return Response({"details": "Completed delete history_pest!"}, status=status.HTTP_200_OK)
        return Response({"error_message": "history_water id is not defined!"}, status=status.HTTP_400_BAD_REQUEST)
    





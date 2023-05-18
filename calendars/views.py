from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import Calendar
from rest_framework.viewsets import ModelViewSet
from .serializers import CalendarSerializer


class CheckAvailabilityAPIView(APIView):
    def post(self, request):
        user = request.user
        data = request.data
        start_datetime = data.get('start_datetime')
        end_datetime = data.get('end_datetime')

        if Calendar.objects.filter(user=user).filter(
            Q(start_datetime__lt=end_datetime) & Q(end_datetime__gt=start_datetime)
        ).exists():
            return Response({'error': 'User is not available at the provided date and time.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'User is available at the provided date and time.'}, status=status.HTTP_200_OK)



class CalendarViewSet(ModelViewSet):
    serializer_class = CalendarSerializer
    queryset = Calendar.objects.all().order_by('-created_at')

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)


class DeleteMeetingAPIView(APIView):
    def delete(self, request, pk):
        user = request.user

        try:
            meeting = Calendar.objects.get(pk=pk, user=user)
            meeting.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Calendar.DoesNotExist:
            return Response({'error': 'Meeting not found.'}, status=status.HTTP_404_NOT_FOUND)


class UpdateMeetingAPIView(APIView):
    def put(self, request, pk):
        user = request.user
        data = request.data

        try:
            meeting = Calendar.objects.get(pk=pk, user=user)
        except Calendar.DoesNotExist:
            return Response({'error': 'Meeting not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CalendarSerializer(instance=meeting, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

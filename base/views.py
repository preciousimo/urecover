from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.conf import settings
from django.core.mail import send_mail
from .models import Booking
from .serializers import BookingSerializer

class BookCounselorView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            # Send email to user and counselor
            send_mail(
                subject="Counseling Session Booking Confirmation",
                message=f"Thank you for booking a session. Details:\n{serializer.data}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[serializer.data['email'], 'counselor@example.com'],
                fail_silently=False
            )
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

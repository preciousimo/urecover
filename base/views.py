from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Booking
from .serializers import BookingSerializer

class BookCounselorView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def send_html_email(self, template_name, context, subject, recipient_list):
        html_content = render_to_string(f'emails/{template_name}.html', context)
        text_content = f"Counseling Session Booking\n\nName: {context['booking'].first_name} {context['booking'].last_name}\nCounseling Area: {context['booking'].counseling_area}"
        
        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=settings.EMAIL_HOST_USER,
            to=recipient_list
        )
        email.attach_alternative(html_content, "text/html")
        return email.send()

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            booking = serializer.save()
            
            # Send confirmation email to client
            self.send_html_email(
                template_name='booking_confirmation',
                context={'booking': booking},
                subject="Your Counseling Session Booking Confirmation",
                recipient_list=[booking.email]
            )
            
            # Send notification email to counselor
            self.send_html_email(
                template_name='counselor_notification',
                context={'booking': booking},
                subject=f"New Counseling Session Booking - {booking.counseling_area}",
                recipient_list=['collegecounselloract@gmail.com']
            )
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
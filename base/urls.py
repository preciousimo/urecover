from django.urls import path
from base.views import BookCounselorView

urlpatterns = [
    path('book-counselor/', BookCounselorView.as_view(), name='book_counselor'),
]

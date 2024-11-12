from django.db import models

class Booking(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    whatsapp_number = models.CharField(max_length=15)
    email = models.EmailField()
    counseling_area = models.CharField(max_length=100)
    contact_method = models.CharField(max_length=100)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.counseling_area}"

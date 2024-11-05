from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from users.manager import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('counsellor', 'Counsellor'),
        ('super_admin', 'Super Admin') 
    )
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    full_name = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, null=True, blank=True)
    counsellor = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='clients')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.full_name:
            self.full_name = f"{self.first_name} {self.last_name}".strip()
        super(User, self).save(*args, **kwargs)

    @property
    def role_display(self):
        return dict(self.ROLE_CHOICES).get(self.role, 'Unknown')

    def activate_user(self):
        if not self.is_active:
            self.is_active = True
            self.save()

    def deactivate_user(self):
        if self.is_active:
            self.is_active = False
            self.save()
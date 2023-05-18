from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from backend.utils import get_currency_by_location

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)
    


class User(AbstractUser):
    username = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_("email address"), unique=True)
    date_of_birth = models.DateField(_('Date of Birth'), null=True, blank=True)
    primary_contact_number = PhoneNumberField(_('Primary Contact Number'), unique=True)
    secondary_contact_number = PhoneNumberField(_('Secondary Contact Number'), blank=True, null=True)
    currency = models.CharField(max_length=3, validators=[RegexValidator(regex='^[A-Z]{3}$', message='Currency should be in uppercase and 3 characters.')])
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    def save(self, *args, **kwargs):
        if not self.currency:
            ip_address = self.request.META.get('REMOTE_ADDR')  # Replace with the actual user's IP address
            self.currency = get_currency_by_location(ip_address)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "user    "
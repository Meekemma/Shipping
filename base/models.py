from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        """
        Creates, saves, and returns a User with the given email, first name, last name, and password.
        """
        if not email:
            raise ValueError('email is required')
        if not first_name:
            raise ValueError('first name is required')
        if not last_name:
            raise ValueError('last name is required')
        
        email =self.normalize_email(email).lower()

        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self.db)
        return user


    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(email=email, first_name=first_name, last_name=last_name, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.is_verified = True
        user.save(using=self._db)
        return user
    

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super(User, self).save(*args, **kwargs)

    



STATUS_CHOICES = [
    ('in_transit', 'In Transit'),
    ('delivered', 'Delivered'),
    ('processing', 'Processing'),
    ('shipped', 'Shipped'),
    ('pending', 'Pending'),
    ('cancelled', 'Cancelled'),
]

TYPE_CHOICES = [
    ('family_luggage', 'Family Luggage'),
    ('commercial_goods', 'Commercial Goods'),
    ('documents', 'Documents'),
    ('electronics', 'Electronics'),
    ('furniture', 'Furniture'),
    ('others', 'Others'),
]

MODE_CHOICES = [
    ('air', 'Air'),
    ('sea', 'Sea'),
    ('land', 'Land'),
    ('rail', 'Rail'),
]

FEE_CHOICES = [
    ('cash', 'Cash'),
    ('credit_card', 'Credit Card'),
    ('mobile_money', 'Mobile Money'),
    ('bank_transfer', 'Bank Transfer'),
]

def generate_tracking_id():
    return f"SHIP-{str(uuid.uuid4())[:8].upper()}"

class Shipment(models.Model):
    tracking_id = models.CharField(max_length=20, unique=True, default=generate_tracking_id)
    sender_name = models.CharField(max_length=255)
    receiver_name = models.CharField(max_length=255)
    phone_number = PhoneNumberField()
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    current_location = models.CharField(max_length=255, blank=True, null=True)
    receiver_address = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    luggage_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='family_luggage')
    mode = models.CharField(max_length=50, choices=MODE_CHOICES, default='land')
    fee = models.CharField(max_length=50, choices=FEE_CHOICES, default='cash')
    book_date = models.DateField(blank=True, null=True)
    pick_up_date = models.DateField(blank=True, null=True)
    expected_delivery_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Shipment {self.tracking_id} - {self.status}"

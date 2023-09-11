from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('customer', 'Customer'),
    ]
    
    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default='customer',
    )

    # Additional fields for user signups
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username

# Create your models here.
class MilkCenter(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)  # You can adjust the max_length as needed
    address = models.TextField()
    price_of_milk = models.DecimalField(max_digits=10, decimal_places=2)  # Assuming price is a decimal value
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class MilkPurchase(models.Model):
    milk_center = models.ForeignKey('MilkCenter', on_delete=models.CASCADE)
    purchase_date = models.DateField()
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_liter = models.DecimalField(max_digits=10, decimal_places=2)
    LR = models.DecimalField(max_digits=10, decimal_places=2)
    Fat = models.DecimalField(max_digits=10, decimal_places=2)
    SNF = models.DecimalField(max_digits=10, decimal_places=2)
    price_on_TS = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"- {self.milk_center} - {self.purchase_date}"
    

class MilkSale(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    purchase_date = models.DateField()
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_liter = models.DecimalField(max_digits=10, decimal_places=2)
    LR = models.DecimalField(max_digits=10, decimal_places=2)
    Fat = models.DecimalField(max_digits=10, decimal_places=2)
    SNF = models.DecimalField(max_digits=10, decimal_places=2)
    price_on_TS = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"- {self.customer} - {self.purchase_date}"
    

class MakePayment(models.Model):
    milk_center = models.ForeignKey('MilkCenter', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50)
    # reference_number = models.CharField(max_length=100, unique=True)
    notes = models.TextField(blank=True, null=True)
    payment_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment #{self.id} - {self.amount}"
    

class ReceivedPayment(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    amount_received = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50)
    # reference_number = models.CharField(max_length=100, unique=True)
    notes = models.TextField(blank=True, null=True)
    received_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Received Payment #{self.id} - {self.customer} - {self.amount_received}"


class Stor(models.Model):
    milk_storage=models.DecimalField(max_digits=100, decimal_places=2, default=0.0)
    balance=models.DecimalField(max_digits=100, decimal_places=2, default=0.0)
    expance=models.DecimalField(max_digits=100, decimal_places=2,null=True)

    def __str__(self):
        return 'Storage'
    
class Expence(models.Model):
    expence_name=models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.expence_name
    
class CustomerExpence(models.Model):

    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    date = models.DateField()
    expence_type=models.TextField(blank=True, null=True)
    expence_amount=models.IntegerField(null=True)

    def __str__(self):
        return self.customer.name
    
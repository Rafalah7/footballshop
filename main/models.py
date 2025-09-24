import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('shoes', 'Shoes'),
        ('jerseys', 'Jerseys'),
        ('ball', 'Ball'),
        ('socks', 'Socks'),
        ('bottle', 'Bottle'),
        ('bandaid', 'Bandaid'),
        ('bag', 'Bag')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    @property
    def is_expensive_item(self):
        return self.price > 1000000

    def discount_price(self, discount):
        if self.is_expensive_item:
            return self.price * (1 - discount)
        return self.price
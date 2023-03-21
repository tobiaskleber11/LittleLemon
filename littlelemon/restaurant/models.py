from django.db import models

# Create your models here.
class Booking(models.Model):
    ID = models.IntegerField(max_length=11 , primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(max_length=6)
    BookingDate = models.DateTimeField()

    def __int__(self): 
        return self.ID
class Menu(models.Model):
    ID = models.IntegerField(max_length=5, primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField(max_length=5)

    def __str__(self):
        return f'{self.title} : {str(self.price)}'

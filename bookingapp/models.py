from django.db import models

# Create your models here.

class Bookings(models.Model):

    ROOM_TYPES = (
        ('SR', 'Standard'),
        ('DR', 'Deluxe'),
        ('SD', 'Super Deluxe'),
        ('TR', 'Tent'),
    )

    booking_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)
    days = models.IntegerField()
    adhar_no = models.CharField(max_length=100)
    booking_date = models.DateTimeField()
    status = models.CharField(max_length=100)
    no_of_persons = models.IntegerField()
    room_type = models.CharField(max_length=2, choices=ROOM_TYPES)
    


    def __str__(self):
        return self.Name

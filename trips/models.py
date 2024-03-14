from django.db import models
from django.contrib.auth.models import User
from travellerprofile.models import Traveller
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class Trip(models.Model):
    """
    Stores an individual trip, related to Traveller model
    """
    REGIONS = ((0, "UK",), (1, "Europe"),
     (2, "Asia"), (3, "Oceania"),
      (4, "North America"), (5, "South America"),
       (6, "Africa"), (7, "Middle East"))
    ACCOMM_OPTIONS = ((0, "Tent"), (1, "Caravan"), (2, "Camper Van"),
    (3, "Hotel/Booked Room"))

    name = models.CharField(max_length=100, unique=True)
    planner = models.ForeignKey(Traveller, on_delete=models.CASCADE, related_name="trips_planned")
    itinerary = models.TextField(max_length=1000)
    region = models.IntegerField(choices=REGIONS, default=0)
    accomm_type = models.IntegerField(choices=ACCOMM_OPTIONS, blank=True)
    interests = models.CharField(max_length=150, blank=True)
    startDate = models.DateField(blank=True)
    endDate = models.DateField(blank=True)
    trip_photo = models.ImageField(upload_to='tripImages/', blank=True, default='placeholder')
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk}: {self.name} in {self.region} planned by {self.planner.user}"
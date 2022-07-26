from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


def unoccupied():
    return User.objects.get(id=2)

class Address(models.Model):
    occupant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=unoccupied,
        on_delete=models.SET_DEFAULT,    
    )
    street_address = models.TextField()
    zipCode = models.TextField()
    state = models.TextField()
    city = models.TextField()

    def __str__(self):
        return str(self.occupant.first_name) + " " + self.zipCode
from django.db import models
from django.contrib.auth.models import User #pylint:disable=(imported-auth-user)
from django.db.models.deletion import CASCADE

class Player(models.Model):
    """Player Model
    Args:
        models (OneToOneField): The user information for the Player
        bio (CharField): The bio of the user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)

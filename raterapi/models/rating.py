from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator


class Rating(models.Model):
    """Join model for Games and Players
    """

game = models.ForeignKey("Game", on_delete=models.CASCADE)
player = models.ForeignKey("Player", on_delete=models.CASCADE)
rating = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])

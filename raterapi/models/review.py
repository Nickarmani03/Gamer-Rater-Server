from django.db import models
from django.db.models.deletion import CASCADE

class Review(models.Model):
    """Review Model
    Fields:
  stars (IntegerField): value of how good the review is
    """
game = models.ForeignKey("Game", on_delete=models.CASCADE)
player = models.ForeignKey("Player", on_delete=models.CASCADE)
review = models.CharField(max_length=200)

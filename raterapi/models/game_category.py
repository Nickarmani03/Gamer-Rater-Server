from django.db import models
from django.db.models.deletion import CASCADE

class GameCategory(models.Model):
    """GameCategory Model  
    Fields:
        game (ForeignKey): the game associated with the event Join model for Games and Players

    """
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

from django.db import models


class Game(models.Model):
    """Game Model
    Fields:
    title (CharField): The name of the game
    description (CharField): The description of the game
    designer (ForeignKey): The creator of the game
    year_released (IntegerField): when the game was released
    number_of_players (IntegerField): The max number of players of the game
     time_to_play (DurationField): how long they get to play the game
    age_recommended (IntegerField): how old qa player shopuld be to play this game
    """
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    designer = models.CharField(max_length=50)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    time_to_play = models.DurationField()
    age_recommended = models.IntegerField()
    categories = models.ManyToManyField("Category", through="GameCategory", related_name="categories")


from django.db import models

class Category(models.Model):
    """Category model
    Fields:
        label (CharField): name of the game type
    """
    label = models.CharField(max_length=50)

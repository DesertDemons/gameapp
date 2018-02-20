from django.db import models

platform_choice = (
		('PC', 'PC'),
		('PS', 'PS'),
		('Nintendo', 'Nintendo'),
		('XBOX', 'XBOX'),
	)

# Create your models here.
class Game(models.Model):
	name = models.CharField(max_length=250)
	release_date = models.DateField()
	platforms = models.CharField(max_length=50, choices=platform_choice)
	multiplayer = models.BooleanField(default=False)
	image = models.ImageField()
	


	def __str__(self):
		return self.name
from django.db import models
from django.db.models import CharField

# Create your models here.
class Pet(models.Model):
	SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
	name = models.CharField(max_length = 100)
	submitter = models.CharField(max_length = 100)
	specices = models.CharField(max_length = 100)
	breed = models.CharField(max_length = 30, blank = True)
	description = models.TextField()
	sex = models.CharField(max_length=10, choices = SEX_CHOICES, blank=True)
	submission_date = models.DateTimeField(null=True)
	age = models.IntegerField(null=True)
	vaccinations = models.ManyToManyField('Vaccine', blank=True)


class Vaccine(models.Model):
	name = models.CharField(max_length= 50)

	def __str__(self):
		return self.name
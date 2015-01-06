from django.db import models

# Create your models here.
class Registration(models.Model):
	Player_Id = models.CharField(max_length=50)
	full_name = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	DOB = models.DateTimeField('Date of birth')
	registration_date = models.DateTimeField('Date of Registration')
	gender = models.CharField(max_length=50)
	address = models.CharField(max_length=100)
	nationality = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	pincode = models.IntegerField(default=0)
	mobile = models.IntegerField(max_length=12) 
	email = models.EmailField()
	question = models.CharField(max_length=100)
	last_club_played = models.CharField(max_length=50)
	last_league = models.CharField(max_length=100)
	date_last_register = models.DateTimeField('Date of lastreg')
	date_last_played = models.DateTimeField('Date of lastplayed')
	salary = models.FloatField()
	def __str__(self):
		return self.Player_Id
# class Apparels(models.Model):
# 	apparels_id = models.IntegerField(max_length=18)
# 	product = 
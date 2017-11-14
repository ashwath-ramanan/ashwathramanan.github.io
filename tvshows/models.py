from django.db import models
from django.utils import timezone


class Tvseries(models.Model):
	user = models.ForeignKey('auth.User')
	title=models.CharField(max_length=200)
	genre = models.CharField(max_length=100)
	creator = models.CharField(max_length=250)
	numberofseasons=models.IntegerField(default=0)
	
	plink=models.CharField(max_length=200)
	def __str__(self):
		return self.title+'-'+self.creator
	likes=models.PositiveIntegerField(default=0)
 
	def total_likes(self):
		return self.likes.count()
	

	dislikes=models.PositiveIntegerField(default=0)

	def total_dislikes(self):
		return self.dislikes.count()

	flags=models.PositiveIntegerField(default=0)

	def total_flags(self):
		return self.flags.count(self)

   
class Seasons(models.Model):
	seasontitle=models.ForeignKey(Tvseries)
	season=models.IntegerField()
	plink = models.CharField(max_length=2000)
	ylink = models.CharField(max_length=2000)
	def __str__(self):
		return self.seasontitle.title
	









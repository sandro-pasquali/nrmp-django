from django.db import models

class Candidate(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name

class Program(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name

class Ranking(models.Model):
	candidate = models.ForeignKey(Candidate)
	program = models.ForeignKey(Program)
	rankofcandidate = models.IntegerField()
	rankofprogram = models.IntegerField()
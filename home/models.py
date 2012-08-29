from django.db import models


class Candidate(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

class Program(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

class CandidateRanklist(models.Model):
	candidate = models.ForeignKey(Candidate)
	program = models.ManyToManyField(Program)
	program_rank = models.IntegerField()

class ProgramRanklist(models.Model):
	program = models.ForeignKey(Program)
	candidate = models.ManyToManyField(Candidate)
	candidate_rank = models.IntegerField()
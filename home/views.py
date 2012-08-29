from django.template import Context, loader
from django.http import HttpResponse
from home.models import Candidate, Program


def index(request):
	all_candidates = Candidate.objects.all().order_by('name')
	all_programs = Program.objects.all().order_by('name')
	t = loader.get_template('home/index.html')
	c = Context({
		'all_candidates': all_candidates,
		'all_programs': all_programs,
	})
	return HttpResponse(t.render(c))

def candidate(request, candidate_id):
	return HttpResponse("You are looking at details for candidate %s." % candidate_id)

def program(request, program_id):
	return HttpResponse("You are looking at details for program %s." % program_id)

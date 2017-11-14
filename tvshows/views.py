from django.shortcuts import render
from .models import Tvseries,Seasons
from django.template import loader
from django.http import HttpResponse

def index(request):
	all_series = Tvseries.objects.all()
	template = loader.get_template('tvshows/home.html')
	context = {'all_series': all_series}
	return HttpResponse(template.render(context, request))

def seasons(request, Tvseries_id):
	season = Seasons.objects.filter(id=Tvseries_id)
	"""try:
		anim = Animeseries.objects.get(pk=animeseries_id)
	except Animeseries.DoesNotExist:
		raise Http404("Anime Does not exist")"""
	return render(request, 'tvshows/seasons.html', {'season': season})
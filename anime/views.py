from django.http import Http404
from django.shortcuts import render
from .models import Animeseries,Arcs
from django.template import loader
from django.http import HttpResponse

def home(request):
	all_anime = Animeseries.objects.all()
	context = {'all_anime': all_anime}
	return render(request, 'anime/home.html', context)

def arc(request, animeseries_id):
	arcs = Arcs.objects.filter(id=animeseries_id)
	"""try:
		anim = Animeseries.objects.get(pk=animeseries_id)
	except Animeseries.DoesNotExist:
		raise Http404("Anime Does not exist")"""
	return render(request, 'anime/arcs.html', {'arcs': arcs})


	
	



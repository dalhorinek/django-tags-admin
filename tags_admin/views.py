from django.http import HttpResponse
from django.utils import simplejson
from taggit.models import Tag

def list_tags(request):
	tags = Tag.objects.filter(name__istartswith=request.GET.get('term', "")).values_list('name', flat=True)
	
	return HttpResponse(simplejson.dumps(list(tags)), mimetype='application/json')

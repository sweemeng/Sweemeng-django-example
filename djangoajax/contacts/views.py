from django.http import HttpResponse
from django.core import serializers
from contacts.models import Contacts
# Create your views here.

def contacts_ajax(request):
    data = serializers.serialize('json',Contacts.objects.all())
    return HttpResponse(data,mimetype='application/json')
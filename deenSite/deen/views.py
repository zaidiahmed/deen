from django.db import models
from django.shortcuts import render_to_response
 
class posts(models.Model):
	FirstName = models.CharField(max_length = 30)
	LastName = models.CharField(max_length = 30)
	Address1 = models.CharField(max_length = 30)
	Address2 = models.CharField(max_length = 30)
	City = models.CharField(max_length = 30)
	State = models.CharField(max_length = 30)
	bodytext = models.TextField()
	timestamp = models.DateTimeField()

def home(request):
	return render_to_response('index.html')

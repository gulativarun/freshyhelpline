from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def welcome(request):
	return HttpResponse("<br/><h1>HELL YEAH WELCOME HERE BROTHER.</h1><br/><h1> JUST WAIT UNTILL ITS DONE... SEE YOU SOON BRUH</h1>")
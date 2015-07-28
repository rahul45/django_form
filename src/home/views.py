from django.shortcuts import render
from django.http import HttpResponse

def index(req):
	return render(req,"index.html",{})



'''def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r'% request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)'''

def login(req): 
	if req.GET['name']=='rahul' and req.GET['pass'] == 'password':
		message = "you successfully login here now"
	else:
		message ="you have entered wrong user name"
	return HttpResponse(message)
	
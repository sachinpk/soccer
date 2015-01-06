from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
import os
from django.template import RequestContext
@csrf_protect
def login(request):
	BASE_DIR = os.path.dirname(os.path.dirname(__file__))
	print BASE_DIR
	state = "Please Login"
	username = password = ''
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				state = "You're successfully logged in!"
			else:
				state = "Your account is not active, please contact the site"
		else:
			state = "username/password incorrect"
	c = {'state':state, 'username': username}
	return render_to_response('auth.html',c,context_instance=RequestContext(request))

# Create your views here.

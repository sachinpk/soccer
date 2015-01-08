from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate
from django.contrib.auth import login as as_login
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.core.urlresolvers import reverse
@csrf_exempt
def login(request):
	state = "Please Login"
	username = password = ''
	if request.method=='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				as_login(request,user)
				state = "You're successfully logged in!"
				return HttpResponseRedirect(reverse('sadmin:test'))
			else:
				state = "Your account is not active, please contact the site"
		else:
			state = "username/password incorrect"
	c = {'state':state, 'username': username}
	return render(request,'socceradmin/login.html',c)


def test(request):
	return render(request,'socceradmin/4.html')
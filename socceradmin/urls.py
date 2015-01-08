from django.conf.urls import patterns,url
from socceradmin import views
urlpatterns = patterns(
	'',
	url(r'^login',views.login,name='login'),
	url(r'^test',views.test,name='test')
	

)
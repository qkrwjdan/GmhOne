
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ViewOnRoad/',include('ViewOnRoad.urls')),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout', kwargs={'next_page': '/ViewOnRoad'}),
]

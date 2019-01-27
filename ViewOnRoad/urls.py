from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$',views.ViewOnRoad_index,name='ViewOnRoad_index'),
   url(r'^signup/$',views.ViewOnRoad_signup,name='ViewOnRoad_signup'),
   url(r'^notice/$',views.ViewOnRoad_notice,name='ViewOnRoad_notice'),
   
]

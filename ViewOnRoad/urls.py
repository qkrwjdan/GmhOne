from django.conf.urls import url
from . import views


urlpatterns = [
   url(r'^$',                   views.ViewOnRoad_index,      name='ViewOnRoad_index'),
   url(r'^signup/$',            views.ViewOnRoad_signup,     name='ViewOnRoad_signup'),
   url(r'^notice/$',            views.ViewOnRoad_notice,     name='ViewOnRoad_notice'),
   url(r'^fileuploadtest/$',    views.ViewOnRoad_fileUpload, name='ViewOnRoad_fileUpload'),
   url(r'^longway/$',           views.ViewOnRoad_longWay,    name='ViewOnRoad_longWay'),
   url(r'^storyonroad/$',       views.ViewOnRoad_storyonroad,name="ViewOnRoad_storyonroad"),
   url(r'^longway/(?P<pk>\d+)/$',views.ViewOnRoad_detail,    name="ViewOnRoad_detail"),

]


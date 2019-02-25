from django.conf.urls import url
from . import views


urlpatterns = [
   url(r'^$',                   views.ViewOnRoad_index,      name='ViewOnRoad_index'),
   url(r'^signup1/$',           views.ViewOnRoad_signup1,     name='ViewOnRoad_signup1'),
   url(r'^signup2/$',           views.ViewOnRoad_signup2,     name='ViewOnRoad_signup2'),
   url(r'^signup3/$',           views.ViewOnRoad_signup3,     name='ViewOnRoad_signup3'),
   url(r'^signup4/$',           views.ViewOnRoad_signup4,     name='ViewOnRoad_signup4'),  
   url(r'^notice/$',            views.ViewOnRoad_notice,     name='ViewOnRoad_notice'),
   url(r'^fileupload(?P<pk>[1-3])$',views.ViewOnRoad_fileupload, name='ViewOnRoad_fileupload'),
   url(r'^longway/$',           views.ViewOnRoad_longWay,    name='ViewOnRoad_longWay'),
   url(r'^storyonroad/$',       views.ViewOnRoad_storyonroad,name="ViewOnRoad_storyonroad"),
   url(r'^longway/(?P<pk>\d+)/$',views.ViewOnRoad_detail,    name="ViewOnRoad_detail"),
   url(r'^profile/$',            views.ViewOnRoad_profile,    name="ViewOnRoad_profile"),
   url(r'^roadview/$',          views.ViewOnRoad_roadview,    name="ViewOnRoad_roadview"),
   
]


from django.conf.urls import url
from . import views
from .views import UserCreateView


urlpatterns = [
   url(r'^$',                              views.ViewOnRoad_index,                name='ViewOnRoad_index'),
   url(r'^signup1/$',                      views.ViewOnRoad_signup1,              name='ViewOnRoad_signup1'),
   url(r'^signup2/$',                      views.ViewOnRoad_signup2,              name='ViewOnRoad_signup2'),
   url(r'^signup3/$',                      UserCreateView,                        name='register'),
   url(r'^signup4/$',                      views.ViewOnRoad_signup4,              name='ViewOnRoad_signup4'),
   url(r'^notice/$',                       views.ViewOnRoad_notice,               name='ViewOnRoad_notice'),
   url(r'^fileupload(?P<pk>[1-3])$',       views.ViewOnRoad_fileupload,           name='ViewOnRoad_fileupload'),
   url(r'^storyonroad/$',                  views.ViewOnRoad_storyonroad,          name="ViewOnRoad_storyonroad"),
   url(r'^storyonroad/(?P<pk>\d+)/$',      views.ViewOnRoad_storyonroad_detail,   name="ViewOnRoad_storyonroad_detail"),
   url(r'^longway/$',                      views.ViewOnRoad_longWay,              name='ViewOnRoad_longWay'),
   url(r'^longway/(?P<pk>\d+)/$',          views.ViewOnRoad_longway_detail,       name="ViewOnRoad_longway_detail"),
   url(r'^roadview/$',                     views.ViewOnRoad_roadview,             name="ViewOnRoad_roadview"),
   url(r'^roadview/(?P<pk>\d+)/$',         views.ViewOnRoad_roadview_detail,      name="ViewOnRoad_roadview_detail"),
   url(r'^profile/$',                      views.ViewOnRoad_profile,              name="ViewOnRoad_profile"),
   url(r'^questions/$',                    views.ViewOnRoad_questions,            name="ViewOnRoad_questions"),
   url(r'^questions/(?P<pk>\d+)/$',        views.ViewOnRoad_question_detail,     name="ViewOnRoad_question_detail"),
   url(r'^ask/$',                          views.ViewOnRoad_ask,                  name="ViewOnRoad_ask" ),
]
    
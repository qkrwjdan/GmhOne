from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   url(r'^$',views.ViewOnRoad_index,name='ViewOnRoad_index'),
   url(r'^signup/$',views.ViewOnRoad_signup,name='ViewOnRoad_signup'),
   url(r'^notice/$',views.ViewOnRoad_notice,name='ViewOnRoad_notice'),
   url(r'^fileuploadtest/$',views.ViewOnRoad_fileUpload,name='ViewOnRoad_fileUpload'),
   url(r'^longway/$',views.ViewOnRoad_longWay,name='ViewOnRoad_longWay'),
   url(r'^signin/$',views.ViewOnRoad_signin,name="ViewOnRoad_signin"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

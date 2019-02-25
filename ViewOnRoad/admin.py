from django.contrib import admin
from .models import storyonroad_uploadFile_model,longway_uploadFile_model,roadview_uploadFile_model,SignUp,UploadFile
# Register your models here.

admin.site.register(UploadFile)
admin.site.register(SignUp)
admin.site.register(roadview_uploadFile_model)
admin.site.register(longway_uploadFile_model)
admin.site.register(storyonroad_uploadFile_model)



from django.contrib import admin
from django.urls import path,include
from django.urls import re_path as url
from . import views
from django.conf import settings
#from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
#from django.contrib.static.urls import static, staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('App_Login.urls')),
    path('blog/', include('App_Blog.urls')),
    path('', views.index, name = 'index'),
]

#urlpatterns += static()
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL,
#    document_root=settings.MEDIA_ROOT)

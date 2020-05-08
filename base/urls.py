
from django.contrib import admin
from django.urls  import path, include
from django.conf.urls.static  import static
from django.conf  import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('guests.urls')),
    path('api/',   include('rest_framework.urls')),
    path('vue/', index_app),

    # path('admin/api',   admin.site.urls),

    path('management/',include('management.urls')),
    path('main/',include('mainpage.urls')),
    path('feedback/', include('feedback.urls')),
    path('waitlist/', include('waitlist.urls')),
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),

]

urlpatterns += staticfiles_urlpatterns()
if(settings.DEBUG):
    urlpatterns+=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

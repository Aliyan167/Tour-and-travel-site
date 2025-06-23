
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from root.settings import ENVIRONMENT, MEDIA_ROOT, STATIC_ROOT
from src.core.handlers import (
    handler404, handler500
)

urlpatterns = []

""" HANDLERS ------------------------------------------------------------------------------------------------------- """
handler404 = handler404
handler500 = handler500

""" INTERNAL REQUIRED APPS ----------------------------------------------------------------------------------------- """
urlpatterns += [
    path('', include('src.web.urls')),
    path('', include('src.api.urls')),


]

""" EXTERNAL REQUIRED APPS ----------------------------------------------------------------------------------------- """
urlpatterns += [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('blog/', include(('src.web.blog.urls', 'blog'), namespace='blog')),
    path('tour/', include(('src.web.tour.urls', 'tour'), namespace='tour')),
    path('destination/', include(('src.web.destination.urls', 'destination'), namespace='destination')),
    path('accounts/', include('allauth.urls')),

]

""" STATIC AND MEDIA FILES ----------------------------------------------------------------------------------------- """
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),



]

""" DEVELOPMENT ONLY -------------------------------------------------------------------------------------------- """
if ENVIRONMENT != 'server':
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls"))
    ]

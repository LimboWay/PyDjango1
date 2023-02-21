from django.contrib import admin
from django.urls import path, include       # re_path, reverse
from core.views import index
# from core.views import view_with_param
# from core.views import view_without_param


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', index, name='home'),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('groups/', include('groups.urls')),

    # path('test/route/param/', view_without_param),          # test/route/param/
    # path(r'test/route/<str:value>/', view_with_param),       # test/route/df;lkjhrlkjgf's/
]

# \n    \t      \b


# https://  www.digitalocean.com   /community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-ru

# https://www.digitalocean.com/

# http://127.0.0.1:45632      /teachers/update/6/

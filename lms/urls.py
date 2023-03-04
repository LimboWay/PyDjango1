from django.contrib import admin
from django.urls import path, include
from core.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('__debug__/', include('debug_toolbar.urls')),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('groups/', include('groups.urls')),
    path('accounts/', include("accounts.urls")),
    path('courses', include('courses.urls')),
    path('accounts/', include('django.contrib.auth.urls'))

]
#
# handler404 = 'core.views.error_404'

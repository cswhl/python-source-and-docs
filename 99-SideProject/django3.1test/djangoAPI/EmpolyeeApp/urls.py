from django.conf.urls import url
from EmpolyeeApp import views
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^department/$', views.departmentApi),
    # url(r'^department/([0-9]+)$', views.departmentApi),
    path('department/<id>', views.departmentApi),

    url(r'^employee/$', views.employeeApi),
    url(r'^employee/([0-9]+)$', views.employeeApi),
    url(r'^saveFile$', views.saveFile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

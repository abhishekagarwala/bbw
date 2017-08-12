from django.conf.urls import include, url
from django.contrib import admin

from apps.dashboard import urls as dashboard_urls

urlpatterns = [
    url(r'^', include(dashboard_urls, namespace='dashboard', app_name="dashboard")),

    url(r'^admin/', include(admin.site.urls)),
]

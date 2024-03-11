"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from accounts import urls
from tracklist.views import (
    tracklist_form,
    deletepage,
    view_assigned_tasks,
    update_task_status,
)

urlpatterns = [
    path("", include("accounts.urls")),
    path("admin/", admin.site.urls),
    path("tracklist/", tracklist_form, name="tracklist"),
    path("deletepage/", deletepage, name="deletepage"),
    path("assigned_tasks/", view_assigned_tasks, name="assigned_tasks"),
    path(
        "update_task_status/<int:task_id>/",
        update_task_status,
        name="update_task_status",
    ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

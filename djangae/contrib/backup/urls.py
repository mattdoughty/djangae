from django.conf.urls import include, url

from . import views

urlpatterns = (
    url(
        '^create-datastore-backup$',
        views.create_datastore_backup,
        name="create_datastore_backup"
    ),
)

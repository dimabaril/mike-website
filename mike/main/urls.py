from django.urls import path

from . import views

app_name = "events"

urlpatterns = [
    path("", views.AboutView.as_view(), name="about"),
    path("about/", views.AboutView.as_view(), name="about"),
    path(
        "<slug:event_type>/",
        views.EventsView.as_view(),
        name="event_list_by_type",
    ),
    path(
        "<slug:event_type>/<int:pk>/",
        views.EventDetailView.as_view(),
        name="event_detail",
    ),
]

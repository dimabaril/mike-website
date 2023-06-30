from django.urls import path

from . import views

app_name = "events"

urlpatterns = [
    path("", views.AboutView.as_view(), name="about"),
    path("about/", views.AboutView.as_view(), name="about"),
    # path("video_design/", views.EventsView.as_view(), name="video_design"),
    # path("av_performance/", views.EventsView.as_view(), name="av_performance"),
    # path("visuals/", views.EventsView.as_view(), name="visuals"),
    # path(
    #     "video_design/<int:pk>/",
    #     views.EventDetailView.as_view(),
    #     name="event_detail",
    # ),
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

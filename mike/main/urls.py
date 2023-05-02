from django.urls import path

from . import views

app_name = "events"

urlpatterns = [
    path("", views.AboutView.as_view(), name="about"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("set_design/", views.EventsView.as_view(), name="set_design"),
    path(
        "interactive_cg/",
        views.InteractiveCg.as_view(),
        name="interactive_cg",
    ),
    path(
        "set_design/<int:pk>/",
        views.EventDetailView.as_view(),
        name="event_detail",
    ),
    # path("main/", views.EventsView.as_view(), name="main"),
    # path("", views.Index, name="index"),
    ##############################
    # path('', views.IndexList.as_view(), name='index'),
    # # path('element/<int:element_id>/',
    # #      views.element_detail, name='element_detail'),
    # path('element/<int:element_id>/',
    #      views.ElementDetail.as_view(), name='element_detail'),
    # # path('create/', views.element_create, name='element_create'),
    # path('create/', views.ElementCreate.as_view(), name='element_create'),
    # # path('element/<int:element_id>/edit/',
    # #      views.element_edit, name='element_edit'),
    # path('element/<int:element_id>/edit/',
    #      views.ElementUpdate.as_view(), name='element_edit'),
    # path('element/<int:element_id>/delete/',
    #      views.ElementDelete.as_view(), name='element_delete'),
]

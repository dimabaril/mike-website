# from django.http import HttpResponse
# from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

# from django.views.generic.base import TemplateView

from .models import Event

# def Index(request):
#     return HttpResponse("Это INDEX")


class AboutView(TemplateView):
    """About."""

    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["event_types"] = Event.TypeChoice.choices
        return context


class EventsView(ListView):
    """Event."""

    # model = Event
    template_name = "main/events.html"
    # context_object_name = "events"
    # fields = ["title", "date", "location", "description"]

    def get_queryset(self):
        """Get queryset."""
        # return Event.objects.filter(type=self.kwargs["event_type"])
        return Event.objects.filter(type=self.kwargs["event_type"]).order_by("-date")

    # def get_context_data(self, **kwargs):
    #     """Get context data."""
    #     context = super().get_context_data(**kwargs)
    #     context["events"] = Event.objects.all()  # [:5]
    #     return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["event_types"] = Event.TypeChoice.choices
        return context


class EventDetailView(DetailView):
    """EventDetailView."""

    model = Event
    template_name = "main/event_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["event_types"] = Event.TypeChoice.choices
        return context

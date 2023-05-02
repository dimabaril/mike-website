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


class InteractiveCg(ListView):
    """InteractiveCg."""

    model = Event
    template_name = "main/interactive_cg.html"


class EventsView(ListView):
    """Event."""

    model = Event
    template_name = "main/set_design.html"
    # context_object_name = "events"
    # fields = ["title", "date", "location", "description"]

    # def get_context_data(self, **kwargs):
    #     """Get context data."""
    #     context = super().get_context_data(**kwargs)
    #     context["events"] = Event.objects.all()  # [:5]
    #     return context


class EventDetailView(DetailView):
    """EventDetailView."""

    model = Event
    template_name = "main/event_detail.html"

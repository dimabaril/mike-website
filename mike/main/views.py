from django.views.generic import DetailView, ListView, TemplateView

from .models import Event


class AboutView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["event_types"] = Event.TypeChoice.choices
        return context


class EventsView(ListView):
    template_name = "main/events.html"

    def get_queryset(self):
        return Event.objects.filter(type=self.kwargs["event_type"]).order_by("-date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["event_types"] = Event.TypeChoice.choices
        return context


class EventDetailView(DetailView):
    model = Event
    template_name = "main/event_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["event_types"] = Event.TypeChoice.choices
        return context

from django.views.generic.base import TemplateView


class AboutView(TemplateView):
    """About."""

    template_name = "about/about.html"


class ContactsView(TemplateView):
    """Contacts."""

    template_name = "about/contacts.html"

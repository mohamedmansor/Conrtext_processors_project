from .models import Website
from django.views.generic import TemplateView


class WebsiteView(TemplateView):
    model = Website
    template_name = "home.html"
    
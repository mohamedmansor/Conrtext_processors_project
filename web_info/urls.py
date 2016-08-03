from django.conf.urls import url
from .views import WebsiteView

urlpatterns = [
    url(r'^$', WebsiteView.as_view(), name='info'),
]

from django.urls import path, re_path,include
from rest_framework.documentation import include_docs_urls
from django.conf.urls.static import static
from django.conf import settings

from .views import AddressView

urlpatterns = [
    path('api/', AddressView.as_view(),name='Address'),

]
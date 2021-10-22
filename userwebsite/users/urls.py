from django.conf.urls import url, include
from .views import dashboard, register

urlpatterns = [
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^oauth/", include("social_django.urls")),
    url(r"^register/", register, name="register"),
]
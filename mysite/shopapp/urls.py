from django.urls import path
from .views import shop_index, about_us

app_name = "shopapp"
urlpatterns = [
    path("", shop_index, name="index"),
    path("about",about_us, name="about"),
]

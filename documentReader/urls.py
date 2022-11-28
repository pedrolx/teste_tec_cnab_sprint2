from django.urls import path
from documentReader import views

urlpatterns = [
    path("results/", views.ReaderViews.as_view())
    ]
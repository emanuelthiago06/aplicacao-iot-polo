from django.contrib import admin
from django.urls import path
from api.views import view_graph, add_point


urlpatterns = [
    path("graph", view_graph, name="plot_graph"),
    path("add-point", add_point, name="add_point")
]
from django.urls import path
from snippets import views

urlpatterns = [
    path("lists/", views.snippet_list),
    path("lists/<int:pk>/", views.snippet_detail),
]

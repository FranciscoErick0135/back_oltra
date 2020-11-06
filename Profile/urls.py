from django.urls import path, re_path

from Profile import views

urlpatterns = [
    re_path(r'^profileModel_url', views.ProfileModelView.as_view()), 
    re_path(r'^profilePerson_url', views.ProfilePersonsView.as_view())
]
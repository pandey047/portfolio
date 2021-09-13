
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('project/', views.project, name='project'),
    path('contact/',views.contact,name='contact'),
    path('search/',views.search_view,name='search')

]
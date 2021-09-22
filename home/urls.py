
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('python/', views.python, name='python'),
    path('blog/', views.blog, name='blog'),
    path('blogpost/<str:slug>/', views.blogpost, name='blogpost'),
    path('java/', views.java, name='java'),
    path('contact/',views.contact,name='contact'),
    path('search/',views.search_view,name='search'),
    path('embeddedHardware/',views.embeddedHardware,name='embeddedHardware'),
    path('embeddedFirmware/',views.embeddedFirmware,name='embeddedFirmware'),

]
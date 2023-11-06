from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.about_view,name='about'),
    path('request/',views.rw_view,name='request'),
    path('requestemail/',views.rw,name='requestemail'),
    path('animation/',views.animation_view,name='animation'),
    path('',views.home_view,name='home'),
    path('animation/',views.animation_view,name='animation')
]

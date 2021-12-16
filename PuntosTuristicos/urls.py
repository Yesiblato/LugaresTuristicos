"""PuntosTuristicos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PuntosTuristicosApp.views import viewsLugares

urlpatterns = [
    path('admin/', admin.site.urls),
    path('LugaresCreated/',viewsLugares.LugaresCreateView.as_view()),
    path('LugaresList/',viewsLugares.LugaresListView.as_view()),
    path('LugaresDetail/<int:pk>/',viewsLugares.LugaresDetailView.as_view()),
    path('LugaresUpdate/<int:pk>/',viewsLugares.LugaresUpdateView.as_view()),
    path('LugaresDelete/<int:pk>/',viewsLugares.LugaresDeleteView.as_view()),
]

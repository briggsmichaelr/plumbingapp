from django.urls import path, include
from . import views

urlpatterns = [
    path('room/', views.room, name = 'room'),
    path('<int:report_id>/where/', views.where, name = 'where'),
    path('<int:report_id>/what/', views.what, name = 'what'),
    path('<int:report_id>/access/', views.access, name = 'access'),
    path('<int:report_id>/when/', views.when, name = 'when'),
    path('<int:report_id>/damage/', views.damage, name = 'damage'),
    path('<int:report_id>/account/', views.account, name = 'account'),
    path('<int:report_id>/confirmation/', views.confirmation, name = 'confirmation'),
]

from django.urls import path, include
from . import views

urlpatterns = [
    path('room/', views.room, name = 'room'),
    path('<int:report_id>/where/', views.where, name = 'where'),
    path('<int:report_id>/account/', views.account, name = 'account'),
    path('<int:report_id>/confirmation/', views.confirmation, name = 'confirmation'),
    #path('<int:product_id>/', views.detail, name = 'detail'),
    #path('<int:product_id>/upvote/', views.upvote, name = 'upvote'),
]

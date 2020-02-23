from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:report_id>/signup/', views.signup, name = 'signup'),
    path('<int:report_id>/login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
]

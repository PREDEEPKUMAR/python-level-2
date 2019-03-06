from django.urls import path
from . import views

urlpatterns = [
    path('<int:resume_id>/', views.resume_display, name='resume_display'),
]
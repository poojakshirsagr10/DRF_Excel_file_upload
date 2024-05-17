from django.urls import path
from .views import StudentView

urlpatterns = [
    path('stu/',StudentView.as_view())
]
from user import views
from django.urls import path

urlpatterns = [
    path('register/', views.UserView.as_view()),
    
]
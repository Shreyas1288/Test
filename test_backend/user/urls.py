from django.urls import path 
from user import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('data/', views.DataList.as_view()),
    path('data/<int:pk>/', views.DataDetail.as_view()),
]

urlpatterns  = format_suffix_patterns(urlpatterns)
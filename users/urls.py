from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', views.UserList.as_view(), name='user-list'),
    path('<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
])

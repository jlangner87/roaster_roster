from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # Root
    path('', views.RoasterList.as_view(), name='roaster_list'),
    # Roaster
    path('roasters', views.RoasterList.as_view(), name='roaster_list'),
    path('roasters/<int:pk>', views.RoasterDetail.as_view(), name='roaster_detail'),
    # Bean
    path('beans/', views.BeanList.as_view(), name="bean_list"),
    path('beans/<int:pk>', views.BeanDetail.as_view(), name="bean_detail"),
    # User
    path('users/', views.UserList.as_view(), name="user_list"),
    path('users/<int:pk>', views.UserDetail.as_view(), name="user_detail")
]

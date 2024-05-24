from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.views import TokenRefreshView
from . import views
from .views import LocationCreateView, ServiceRequestCreate, MessageListCreate


urlpatterns = [
    path('register/', views.UserRegistrationAPIView.as_view()),
    path('login/', views.UserLoginAPIView.as_view()),

    path('user-details/', views.GetUserDetailsAPIView.as_view()),
    path('verify-token/', TokenVerifyView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    
    #location
    path('location/', LocationCreateView.as_view(), name='create_location'),
    
    # Service request
    path('service_request/', ServiceRequestCreate.as_view(), name='service_request'),
    
    # Message
    path('messages/', MessageListCreate.as_view(), name='message-list-create'),
]

from django.urls import path

from account import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register-slash'),
    path('obtain-token/', views.ObtainTokenView.as_view(), name='obtain-token-slash'),
    path('logout/', views.LogoutView.as_view(), name='logout-slash'),
]

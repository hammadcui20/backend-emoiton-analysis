from django.urls import path
from .views import RegisterView, ProfileView, CustomLoginView, UserListView, UserUpdateDeleteView, PerformanceView, \
    ForgotPasswordView, ResetPasswordView, LogoutView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('auth/login/', csrf_exempt(CustomLoginView.as_view()), name='custom_login'),
    path('profile/', ProfileView.as_view(), name='profile'),

    # Admin Dashboard
    path('admin/users/', UserListView.as_view(), name='admin-users'),
    path('admin/users/<int:pk>/', UserUpdateDeleteView.as_view(), name='admin-user-detail'),
    path('admin/performance/', PerformanceView.as_view(), name='admin-performance'),

    # Forgot Password
    path('auth/forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('auth/reset-password/', ResetPasswordView.as_view(), name='reset-password'),

    path('auth/logout/', LogoutView.as_view(), name='logout'),
]

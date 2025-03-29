from django.urls import path
from .views import RegisterView, ProfileView, CustomLoginView, UserListView, UserUpdateDeleteView, PerformanceView, \
     LogoutView
from django.views.decorators.csrf import csrf_exempt
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('auth/login/', csrf_exempt(CustomLoginView.as_view()), name='custom_login'),
    path('profile/', ProfileView.as_view(), name='profile'),

    # Admin Dashboard
    path('admin/users/', UserListView.as_view(), name='admin-users'),
    path('admin/users/<int:pk>/', UserUpdateDeleteView.as_view(), name='admin-user-detail'),
    path('admin/performance/', PerformanceView.as_view(), name='admin-performance'),

    # Forgot Password
    path('auth/forgot-password/', PasswordResetView.as_view(), name='forgot-password'),
    path('auth/reset-password-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
]

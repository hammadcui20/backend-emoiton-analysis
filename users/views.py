from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import RegisterSerializer, UserSerializer
from dj_rest_auth.views import LoginView
from rest_framework.response import Response
from rest_framework import status


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """Custom handling of email uniqueness before calling serializer"""
        email = request.data.get("email")
        print("email", email)
        if User.objects.filter(email=email).exists():
            return Response(
                {"email": ["A user with this email already exists."]},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)


from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from dj_rest_auth.views import LoginView
from rest_framework import status


@method_decorator(csrf_exempt, name='dispatch')
class CustomLoginView(LoginView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        # Modify response data to include role
        if response.status_code == status.HTTP_200_OK:
            response.data["role"] = "admin" if self.user.is_admin_user else "user"
            response.data["email"] = self.user.email
            response.data["username"] = self.user.username
            response.data["dob"] = self.user.dob
            response.data["phone_number"] = self.user.phone_number

        return response


class ProfileView(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


# Admin API's
from rest_framework import generics, status, views
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, PerformanceSerializer

User = get_user_model()


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


from datetime import timedelta
from django.utils.timezone import now


class PerformanceView(generics.GenericAPIView):
    serializer_class = PerformanceSerializer

    def get(self, request, *args, **kwargs):
        total_users = User.objects.count()
        active_users = User.objects.filter(is_active=True).count()
        new_users_last_30_days = User.objects.filter(date_joined__gte=now() - timedelta(days=30)).count()

        data = {
            "total_users": total_users,
            "active_users": active_users,
            "new_users_last_30_days": new_users_last_30_days
        }

        serializer = self.get_serializer(data)
        return Response(serializer.data)


from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView



class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class LogoutView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.auth.delete()
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

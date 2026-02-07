from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from .serializer import ChangePasswordSerializer, RegisterSerializer, UserSerializer


User = get_user_model()


class RegisterView(generics.CreateAPIView):
	serializer_class = RegisterSerializer
	permission_classes = (permissions.AllowAny,)


class UserListView(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (permissions.IsAdminUser,)


class MeView(generics.RetrieveUpdateAPIView):
	serializer_class = UserSerializer
	permission_classes = (permissions.IsAuthenticated,)
<<<<<<< Updated upstream
 
=======

>>>>>>> Stashed changes
	def get_object(self):
		return self.request.user


class ChangePasswordView(generics.UpdateAPIView):
	serializer_class = ChangePasswordSerializer
	permission_classes = (permissions.IsAuthenticated,)

	def get_object(self):
		return self.request.user

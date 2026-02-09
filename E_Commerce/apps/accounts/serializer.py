from django.contrib.auth import get_user_model
from rest_framework import serializers
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = (
			'id',
			'email',
			'first_name',
			'last_name',
			'phone_number',
		)
		read_only_fields = ('id',)


class RegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, min_length=8)

	class Meta:
		model = User
		fields = (
			'email',
			'password',
			'first_name',
			'last_name',
			'phone_number',
			'is_staff',
			'is_active',
		)

	def create(self, validated_data):
		return User.objects.create_user(**validated_data,)


class ChangePasswordSerializer(serializers.Serializer):
	old_password = serializers.CharField(required=True, write_only=True)
	new_password = serializers.CharField(required=True, min_length=8, write_only=True)
	confirm_new_password = serializers.CharField(required=True, min_length=8, write_only=True)

	def validate(self, data):
		if data['new_password'] != data['confirm_new_password']:
			raise serializers.ValidationError("New passwords do not match.")
		return data

	def validate_old_password(self, value):
		user = self.context['request'].user
		if not user.check_password(value):
			raise serializers.ValidationError("Old password is not correct.")
		return value

	def save(self, **kwargs):
		user = self.context['request'].user
		user.set_password(self.validated_data['new_password'])
		user.save()
		return user
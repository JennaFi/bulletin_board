from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from config.settings import EMAIL_HOST_USER
from users.models import User
from users.serializers import UserSerializer

token_generator = PasswordResetTokenGenerator()


class UserCreateAPIView(generics.CreateAPIView):
    """Creation of user"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserDestroyAPIView(generics.DestroyAPIView):
    """Destruction of user"""

    serializer_class = UserSerializer
    queryset = User.objects.all()


class RequestPasswordResetView(APIView):
    """Request password reset"""

    permission_classes = [AllowAny]

    def post(self, request):
        """Send request to email"""

        email = request.data.get('email')
        if email:
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)
            reset_url = request.build_absolute_uri(
                reverse('users:password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
            )
            send_mail(
                subject='Password reset',
                message=f'Follow this link to reset password: {reset_url}',
                from_email=EMAIL_HOST_USER,
                recipient_list=[email],
            )

            return Response({'message': 'Emeil to reset password sent'}, status=status.HTTP_200_OK)
        return Response({'error': 'Email not given'}, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmView(APIView):
    """Confirmation of password resetting"""

    permission_classes = [AllowAny, ]

    def post(self, request):

        uidb64 = request.data.get('uid')
        token = request.data.get('token')
        new_password = request.data.get('new_password')

        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        if token_generator.check_token(user, token):
            user.set_password(new_password)
            user.save()
            return Response({'message': 'The password was successfully changed'})
        else:
            return Response({'error': 'Invalid token or user'}, status=status.HTTP_400_BAD_REQUEST)

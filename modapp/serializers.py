from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer



class CustomRegisterSerializer(RegisterSerializer):
    """Use default serializer except don't user username"""

    username = None

    def get_cleaned_data(self):
        return {
            "password1": self.validated_data.get("password1", ""),
            "password2": self.validated_data.get("password2", ""),
            "email": self.validated_data.get("email", ""),
        }


class CustomLoginSerializer(LoginSerializer):
    """Use default serializer except don't user username"""

    username = None

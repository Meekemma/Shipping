from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import TrackingIDSerializer, ShipmentDetailSerializer
from .models import Shipment
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .swagger_docs import shipment_tracking_view_docs, login_view_docs




@shipment_tracking_view_docs
@api_view(['POST'])
def ShipmentTrackingView(request):
    """
    Handles shipment tracking by accepting a tracking ID and returning shipment details.
    """
    # Validate the tracking ID
    input_serializer = TrackingIDSerializer(data=request.data)
    if input_serializer.is_valid(raise_exception=True):
        tracking_id = input_serializer.validated_data.get('tracking_id')
        shipment = Shipment.objects.get(tracking_id=tracking_id)

        # Serialize the shipment details
        response_serializer = ShipmentDetailSerializer(shipment)
        return Response(response_serializer.data, status=status.HTTP_200_OK)

    return Response(input_serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom serializer for JWT tokens with additional claims.
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['user_id'] = user.id
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        return token
    
    def validate(self, attrs):
        # Normalize the email to lowercase before validation
        attrs['email'] = attrs['email'].lower()
        data = super().validate(attrs)

        # Add extra responses
        data.update({'user_id': self.user.id})
        full_name = f"{self.user.first_name} {self.user.last_name}"
        data.update({'full_name': full_name})
        data.update({'email': self.user.email})
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    """
    Custom view to obtain JWT tokens with additional claims.
    """
    serializer_class = MyTokenObtainPairSerializer

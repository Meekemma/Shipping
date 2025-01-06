from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import TrackingIDSerializer, ShipmentDetailSerializer


# Request example for Swagger documentation
request_example = {
    "tracking_id": "SHIP-AD556690"
}
# Response example for Swagger documentation
response_example_200 = {
    "id": 3,
    "tracking_id": "SHIP-3AA9BBE9",
    "sender_name": "John Doe",
    "receiver_name": "Kate Doe",
    "phone_number": "+2348160855537",
    "origin": "Nigeria",
    "destination": "Canada",
    "current_location": "Lagos",
    "receiver_address": "123, Main Street, Toronto",
    "status": "processing",
    "luggage_type": "family_luggage",
    "mode": "land",
    "fee": "cash",
    "book_date": "2024-12-18",
    "pick_up_date": "2024-12-20",
    "expected_delivery_date": "2024-12-25",
    "created_at": "2024-12-19T01:32:57.892487Z",
    "updated_at": "2024-12-19T01:32:57.892487Z"
}

# Swagger Documentation for ShipmentTrackingView
shipment_tracking_view_docs = swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'tracking_id': openapi.Schema(
                type=openapi.TYPE_STRING, 
                description='The tracking ID of the shipment.'
            )
        },
        required=['tracking_id'],
        example=request_example  
    ),
    responses={
        200: openapi.Response(
            description="Shipment details",
            schema=ShipmentDetailSerializer,  
            examples={"application/json": response_example_200}  
        ),
        400: openapi.Response("Invalid tracking ID provided"),
        404: openapi.Response("Shipment not found"),
    },
    operation_description="Track a shipment using a tracking ID."
)





#Login request example for Swagger documentation
login_request_example = {
    "email": "user@example.com",
    "password": "password123"
}
#Login response example for Swagger documentation
login_response_example_200 = {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "user_id": 1,
    "full_name": "John Doe",
    "email": "user@example.com"
}

login_response_example_401 = {
    "detail": "No active account found with the given credentials"
}

# Swagger Documentation for LoginView
login_view_docs = swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email address'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password'),
        },
        required=['email', 'password'],
        example=login_request_example  
    ),
    responses={
        200: openapi.Response(
            description="Login successful",
            examples={"application/json": login_response_example_200}  
        ),
        401: openapi.Response(
            description="Unauthorized - Invalid credentials",
            examples={"application/json": login_response_example_401}  
        ),
    },
    operation_description="Authenticate a user and return access and refresh tokens along with user information."
)

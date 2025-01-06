from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import PrivateChatRoomSerializer, PrivateMessageSerializer



# Swagger for private_chat_room_list
private_chat_room_list_docs = {
    'get': swagger_auto_schema(
        responses={200: PrivateChatRoomSerializer(many=True)},
        operation_description="Retrieve a list of all private chat rooms."
    ),
    'post': swagger_auto_schema(
        request_body=PrivateChatRoomSerializer,
        responses={
            201: PrivateChatRoomSerializer,
            400: openapi.Response("Invalid data provided"),
        },
        operation_description="Create a new private chat room."
    ),
}

# Swagger for private_chat_room_detail
private_chat_room_detail_docs = {
    'get': swagger_auto_schema(
        responses={200: PrivateChatRoomSerializer},
        operation_description="Retrieve details of a specific private chat room by its ID."
    ),
    'delete': swagger_auto_schema(
        responses={
            204: openapi.Response("Chat room deleted successfully"),
            404: openapi.Response("Chat room not found"),
        },
        operation_description="Delete a specific private chat room by its ID."
    ),
}

# Swagger for private_message_list
private_message_list_docs = {
    'get': swagger_auto_schema(
        responses={200: PrivateMessageSerializer(many=True)},
        operation_description="Retrieve a list of all private messages."
    ),
    'post': swagger_auto_schema(
        request_body=PrivateMessageSerializer,
        responses={
            201: PrivateMessageSerializer,
            400: openapi.Response("Invalid data provided"),
        },
        operation_description="Send a new private message."
    ),
}

# Swagger for private_message_list_by_room
private_message_list_by_room_docs = swagger_auto_schema(
    manual_parameters=[
        openapi.Parameter(
            'room_id', openapi.IN_PATH, description="ID of the chat room",
            type=openapi.TYPE_INTEGER, required=True
        )
    ],
    responses={200: PrivateMessageSerializer(many=True)},
    operation_description="Retrieve a list of messages for a specific private chat room."
)

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PrivateChatRoom, PrivateMessage
from .serializers import PrivateChatRoomSerializer, PrivateMessageSerializer


@api_view(['GET', 'POST'])
def private_chat_room_list(request):
    if request.method == 'GET':
        chat_rooms = PrivateChatRoom.objects.all()
        serializer = PrivateChatRoomSerializer(chat_rooms, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PrivateChatRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def private_chat_room_detail(request, pk):
    chat_room = get_object_or_404(PrivateChatRoom, pk=pk)

    if request.method == 'GET':
        serializer = PrivateChatRoomSerializer(chat_room)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        chat_room.delete()
        return Response({'message': 'Chat room deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def private_message_list(request):
    if request.method == 'GET':
        messages = PrivateMessage.objects.all()
        serializer = PrivateMessageSerializer(messages, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PrivateMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def private_message_list_by_room(request, room_id):
    messages = PrivateMessage.objects.filter(chat_room_id=room_id).order_by('timestamp')
    serializer = PrivateMessageSerializer(messages, many=True)
    return Response(serializer.data)

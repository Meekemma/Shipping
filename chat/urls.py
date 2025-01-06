from django.urls import path
from . import views

urlpatterns = [
    path('chat-rooms/', views.private_chat_room_list, name='chat-room-list'),
    path('chat-rooms/<int:pk>/', views.private_chat_room_detail, name='chat-room-detail'),
    path('messages/', views.private_message_list, name='message-list'),
    path('messages/<int:room_id>/', views.private_message_list_by_room, name='message-list-by-room'),
]

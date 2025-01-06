from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.conf import settings

class PrivateChatRoom(models.Model):
    name = models.CharField(max_length=255, unique=True) 
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='chat_user1',on_delete=models.CASCADE, blank=True, null=True)
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='chat_user2',on_delete=models.CASCADE, blank=True, null=True)
    guest_user = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user1', 'user2', 'guest_user')

    def __str__(self):
        user1_display = self.user1.first_name if self.user1 else "Guest"
        user2_display = self.user2.first_name if self.user2 else self.guest_user or "Guest"
        return f"Chat between {user1_display} and {user2_display}"




class PrivateMessage(models.Model):
    chat_room = models.ForeignKey(PrivateChatRoom, related_name='messages', on_delete=models.CASCADE)  
    sender = models.ForeignKey(settings.AUTH_USER_MODEL,  null=True, blank=True, on_delete=models.CASCADE)  
    guest_sender = models.CharField(max_length=100,null=True,blank=True)
    content = models.TextField()  
    timestamp = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        sender_display = self.sender.first_name if self.sender else self.guest_sender or "Anonymous"
        return f"Message by {sender_display} at {self.timestamp}"
       

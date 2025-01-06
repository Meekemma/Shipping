from django.contrib import admin

from .models import PrivateChatRoom, PrivateMessage

class PrivateMessageInline(admin.TabularInline):
    model = PrivateMessage
    extra = 0  
    fields = ('sender', 'guest_sender', 'content', 'timestamp')  
    readonly_fields = ('sender', 'guest_sender', 'content', 'timestamp')  

@admin.register(PrivateChatRoom)
class PrivateChatRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'user1', 'user2', 'guest_user', 'created_at')  # Include guest_user in display
    search_fields = ('user1__username', 'user2__username', 'guest_user')  # Allow searching by guest_user
    list_filter = ('created_at',)  # You can add filters for guest_user if needed
    inlines = [PrivateMessageInline]

from django.contrib import admin
from .models import Shipment
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User



admin.site.site_header = "XYZ SHIPMENT Administration"
admin.site.site_title = "XYZ SHIPMENT"
admin.site.index_title = "Welcome to XYZ SHIPMENT Admin Panel"





class UserAdmin(BaseUserAdmin):
    list_display = ('id','email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    readonly_fields = ['created_at', 'updated_at']  # Make 'created_at' read-only

admin.site.register(User, UserAdmin)







class ShipmentAdmin(admin.ModelAdmin):
    list_display = (
        'tracking_id',
        'sender_name',
        'receiver_name',
        'receiver_address',
        'origin',
        'destination',
        'current_location',
        'status',
        'luggage_type',
        'mode',
        'fee',
        'book_date',
        'expected_delivery_date',
        'created_at',
    )
    search_fields = (
        'tracking_id',
        'sender_name',
        'receiver_name',
        'origin',
        'destination',
        'current_location',
    )
    list_filter = (
        'status',
        'luggage_type',
        'mode',
        'fee',
        'book_date',
        'pick_up_date',
        'expected_delivery_date',
    )

admin.site.register(Shipment, ShipmentAdmin)

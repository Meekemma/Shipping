from rest_framework import serializers
from .models import Shipment




class TrackingIDSerializer(serializers.Serializer):
    tracking_id = serializers.CharField(max_length=20)

    def validate_tracking_id(self, value):
        try:
            shipment = Shipment.objects.get(tracking_id=value)
        except Shipment.DoesNotExist:
            raise serializers.ValidationError("Invalid Tracking ID. Shipment not found.")
        return value


class ShipmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'

from rest_framework import serializers
from ..models.achat import Achat

class AchatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achat
        fields = '__all__'
        read_only_fields = ['utilisateur']  # 👈 important

    def create(self, validated_data):
        validated_data['utilisateur'] = self.context['request'].user
        return super().create(validated_data)


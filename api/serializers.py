from rest_framework import serializers
from api.models import Search

class SearchSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    query = serializers.CharField(required=True, allow_blank=False, max_length=1024)
    processed = serializers.CharField(default=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new search instance, given the validated data.
        """
        return Search.objects.create(**validated_data)

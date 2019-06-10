import django_rq
from rest_framework import serializers
from api.models import Search
from api.tasks import perform_search

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
        search = Search.objects.create(**validated_data)
        django_rq.enqueue(perform_search, search.id)
        return search

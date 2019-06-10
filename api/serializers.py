import django_rq
from rest_framework import serializers
from api.models import Protein, Result, Search
from api.tasks import perform_search

class ProteinSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    code = serializers.CharField(read_only=True)

    class Meta:
        model = Protein
        fields = '__all__'

class ResultSerializer(serializers.Serializer):
    protein = ProteinSerializer(read_only=True)
    location = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Result
        fields = '__all__'

class SearchSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    query = serializers.CharField(required=True, allow_blank=False, max_length=1024)
    processed = serializers.CharField(default=False)
    result = ResultSerializer(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Search
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new search instance, given the validated data.
        """
        search = Search.objects.create(**validated_data)
        django_rq.enqueue(perform_search, search.id)
        return search

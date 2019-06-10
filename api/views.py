from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from api.models import Search
from api.serializers import SearchSerializer

class SearchViewSet(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 GenericViewSet):
    """
    Create and list endpoints for searches
    """
    queryset = Search.objects.prefetch_related('result', 'result__protein').all()
    serializer_class = SearchSerializer

    def list(self, request, *args, **kwargs):
        """
        List a queryset
        """
        queryset = Search.objects.filter(session_id = request.session.session_key).prefetch_related('result', 'result__protein').all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Create a model instance
        """
        if not request.session.session_key:
            request.session.create()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(session_id=request.session.session_key)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

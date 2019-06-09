from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet
from api.models import Search
from api.serializers import SearchSerializer

class SearchViewSet(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 GenericViewSet):
    """
    Create, list, and read endpoints for searches
    """
    queryset = Search.objects.all()
    serializer_class = SearchSerializer
    # permission_classes = (permissions.IsAuthenticated,)

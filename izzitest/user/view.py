"""
User`s View
"""
from django_filters import rest_framework as filters
from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer


class UserFilter(filters.FilterSet):
    """
    Filter for users
    """
    class Meta:
        model = User
        fields = {
            'registration_date': ['iexact', 'lte', 'gte']  # filter options == <= >=
        }

# pylint: disable=too-many-ancestors
class UserViewSet(viewsets.ModelViewSet):
    """
    User View Set
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter

    def get_queryset(self):
        """
        API query
        :return:
        """
        queryset = User.objects.all()
        query = self.request.GET.get('date')
        if query:
            print('query =', query)
            query = query.strip('/')
            queryset = User.filter(registration_date=query)

        return queryset

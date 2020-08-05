from .models import User
from rest_framework import viewsets
from django_filters import rest_framework as filters
from .serializers import UserSerializer

class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'registration_date':['iexact', 'lte', 'gte']
        }

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter

    def get_queryset(self, *args, **kwargs):
        queryset = User.objects.all()
        query = self.request.GET.get('date')
        if query:
            print('query =', query)
            query = query.strip('/')
            queryset = User.filter(registration_date=query)

        return queryset



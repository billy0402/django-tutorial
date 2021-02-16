from django.contrib.auth.models import User
from rest_framework import viewsets

from .serializers import UserSerializer


# Create your views here.
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

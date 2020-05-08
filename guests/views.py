from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework.decorators import api_view ,APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Guest ,Table
from .serializers import GuestSerializer ,UserSerializer ,TableSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly,IsOwnerOrReadOnly_t
from rest_framework import renderers
from rest_framework.response import Response

class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        guest = self.get_object()
        return Response(guest.highlighted)
    def perform_create(self, serializer):

        serializer.save(owner=self.request.user)


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly_t]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        table = self.get_object()
        return Response(table.highlighted_t)

    def perform_create(self, serializer):
        serializer.save(owner_t=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ApiRoot(APIView):
    def get(self,request,format=None):
        return Response({
            'users':    reverse('users', request=request, format=format),
            'guests': reverse('guests', request=request, format=format),
            'tables': reverse('tables', request=request, format=format),
        })


from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GuestViewSet, UserViewSet, ApiRoot ,TableViewSet
from rest_framework import renderers
from django.urls import path, include
guest_list = GuestViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
guest_detail = GuestViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
guest_highlight = GuestViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

table_list = TableViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
table_detail = TableViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
table_highlight = TableViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])



user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'guests', GuestViewSet)

router.register(r'tables', TableViewSet)
router.register(r'users', UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
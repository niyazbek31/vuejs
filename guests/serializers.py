from rest_framework import serializers
from .models import Guest ,Table
from django.contrib.auth.models import User
class GuestSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='guest-highlight', format='html')

    class Meta:
        model = Guest
        fields = ['url', 'id', 'highlight', 'owner',
                  'name', 'email']

class TableSerializer(serializers.HyperlinkedModelSerializer):
    owner_t = serializers.ReadOnlyField(source='owner_t.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='table-highlight', format='html')


    class Meta:
        model = Table
        fields = ['url', 'id', 'highlight', 'owner_t',
                  'name_guest', 'number_tab','tel_guest']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    guests = serializers.HyperlinkedRelatedField(many=True, view_name='guest-detail', read_only=True)
    tables=  serializers.HyperlinkedRelatedField(many=True, view_name='table-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'guests','tables']
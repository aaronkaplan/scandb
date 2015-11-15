from django.contrib.auth.models import User, Group
from sdb.models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class NetworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Network
        fields = ('netblock', 'name')

class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ('ip', 'network', 'description', 'scannable')

class ScanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scan
        fields = ('name', 'description', 'ts_started', 'ts_finished', 'continuous', 'overall_scor', 'authorized_by')

class ScannerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scanner
        fields = ('name', 'url')

class ScannerModuleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ScannerModule
        fields = ('name', 'url')

class ScannerModuleResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ScannerModuleResult
        fields = ('host', 'scan', 'module', 'score', 'previous_score', 'recommendations_url')



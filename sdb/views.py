from django.shortcuts import render
from django.contrib.auth.models import User, Group
from sdb.models import *
from rest_framework import viewsets
from sdb.serializers import *

# Create your views here.




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all().order_by('netblock')
    serializer_class = NetworkSerializer

class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all().order_by('ip')
    serializer_class = HostSerializer

class ScanViewSet(viewsets.ModelViewSet):
    queryset = Scan.objects.all().order_by('-ts_started')
    serializer_class = NetworkSerializer

class ScannerViewSet(viewsets.ModelViewSet):
    queryset = Scanner.objects.all().order_by('name')
    serializer_class = ScannerSerializer

class ScannerModuleViewSet(viewsets.ModelViewSet):
    queryset = ScannerModule.objects.all().order_by('scanner','name')
    serializer_class = ScannerModuleSerializer

class ScannerModuleResultViewSet(viewsets.ModelViewSet):
    queryset = ScannerModuleResult.objects.all().order_by('scanner','scan','module', 'host','-score', 'previous_score', 'recommendations_url')
    serializer_class = ScannerModuleResultSerializer


from django.db import models
from django.contrib.auth.models import User
from netfields import InetAddressField, NetManager




# Create your models here.
"""
  The network the host is in
"""
class Network(models.Model):
    name                        = models.CharField(max_length=200)
    netblock                    = InetAddressField('Netblock', default='192.168.0.0/24', unique=True)
    objects                     = NetManager()

    def __unicode__(self):
        return str(self.netblock)


"""
  The actual host being scanned
"""
class Host(models.Model):
    ip                          = InetAddressField('IP address', unique=True)
    network                     = models.ForeignKey(Network)    # Host belongs to network
    description                 = models.CharField(max_length=200, null=True, blank=True)       # free text description for the host, comments...
    scannable                   = models.BooleanField('scannable', default=True)
    objects                     = NetManager()




""" 
 The main scan class: contains metadata (time started, time finished) of the scan 
"""
class Scan(models.Model):
    name                        = models.CharField(max_length=200)
    description                 = models.CharField(max_length=10000, null=True, blank=True)
    ts_started                  = models.DateTimeField('starting time',  null=True, blank=True)
    ts_finished                 = models.DateTimeField('finishing time', null=True, blank=True)
    continuous                  = models.NullBooleanField('this scan is continuous?', null=True, blank=True, default=False)
    overall_score               = models.FloatField('overall score', null=True, blank=True)
    authorized_by               = models.ForeignKey(User)




""" 
 The Software used for the scanning. i.e. the scanner itself ("Nessus", "sqlmap", "shodan", ...)
"""
class Scanner(models.Model):
    name                        = models.CharField(max_length=200)
    url                         = models.URLField('URL describing the scanner', null=True, blank=True)

  
""" 
 The (Nessus)/scanner module used for doing the tests. For example Nessus/SQL injection
"""
class ScannerModule(models.Model):
    name                        = models.CharField(max_length=200)
    scanner                     = models.ForeignKey(Scanner)
    description                 = models.CharField(max_length=10000, null=True, blank=True)
    url                         = models.URLField('URL for explanation of the scan module', null=True, blank=True)
   
""" 
 The results of the module for a specific network, scan and scan module
"""
class ScannerModuleResult(models.Model):
    scan                        = models.ForeignKey(Scan)
    scanner                     = models.ForeignKey(Scanner)
    module                      = models.ForeignKey(ScannerModule)
    # XXX FIXME: actually this should be (service,host) - think SNI and Host: fields. It can be the same IP, same port but different "service" a.k.a server name
    host                        = models.ForeignKey(Host)
    score                       = models.FloatField('score', null=True, blank=True)
    previous_score              = models.FloatField('previous score', null=True, blank=True)
    recommendations_url         = models.URLField('Link to a site with recommendations on how to improve the situation', null=True, blank=True)
    # XXX add all the fields of scan results. Might be better to make a separate class for that for all different scanner types (abstract class and inheritance)
    


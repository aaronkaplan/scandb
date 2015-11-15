# ScanDB

This is an initial draft version of a database to keep track of authorized scanning of networks.
The basic idea is that a client authorizes a scan for a specific network. The pentester doing the scan uses one to multiple scanners with multiple scan modules for each IP address in every network range of the client.

Author:
L. Aaron Kaplan <aaron-at-sign-lo-res.org>, done in his spare time.


## EER

Here is an Extended Entity Relationship diagram

```
             authorizes         

                       n +--------+ 
                 / ----- | scan   |
                /        +--------+ 
               /             | m
              /              |
           1 /               | n      scans
    +---------+          +--------+ n      m +-----------+
    | client  |          | scanner|  ------  | network   |
    +---------+          +--------+          +-----------+
                       1 /   | 1               1  |
             is_part_of /    |                   n| is_part_of
 +------------+ n      /     |             1 +-----------+
 |scanModule  |-------/      |             - | host      |
 +------------+              | n       m  /  +-----------+
             1 \      m  +-------------+ /
                ---------| scan result |-
                         +-------------+


```



## Installation

(Assuming you use Ubuntu or Debian)

```bash
sudo apt-get install python-virtualenv
git clone https://github.com/aaronkaplan/scandb.git
cd scandb
virtualenv env
source env/bin/activate
pip install django
pip install psycopg2
pip install djangorestframework
```

Next edit the settings.py file:
```bash
vi scandb/settings.py
```

Change `SECRET_KEY = 'XXXX'` to some very long random string.


Create a postgresql DB:
```bash
sudo -u postgres createdb scandb
```

Download the netfields package:
```bash
git clone https://github.com/jimfunk/django-postgresql-netfields.git netfields
cd netfields
python setup.py install
```




## TODOs
  * add subtable (inheritance!) for:
    * Nessus
    * Nmap
    * Acunetix
    * ...
  * load the most common scanners (see above) as fixtures into the "scanner" table
  * make a script to load Nessus/nmap/... scans into the scan result table
  * find a **comparable** metric  (does not need to be perfect! Just an indication of progress!) for scan results (e.g. a number between 1 and 10). Assign each scan result a metric score.
  * visualise scores (for details as well as aggregated averages) for scans 






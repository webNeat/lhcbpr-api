#!/afs/cern.ch/user/a/amazurov/www/lhcbpr-api/venv/bin/python
import sys, os

sys.path.insert(0, "/afs/cern.ch/user/a/amazurov/www/lhcbpr-api/site")
os.environ['DJANGO_SETTINGS_MODULE'] = "settings"
from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")

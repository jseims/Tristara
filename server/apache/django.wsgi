import os
import sys

path = '/data/tristara/server'
if path not in sys.path:
    sys.path.append(path)

path = '/data/tristara/config'
if path not in sys.path:
    sys.path.append(path)
    
path = '/data/tristara'
if path not in sys.path:
    sys.path.append(path)
    
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


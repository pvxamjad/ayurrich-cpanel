import sys
import os

# Add your Django project's directory to the Python path
sys.path.insert(0, '/home/pxi2rz4br0st/ayur/ayur_rich/')  # Replace with your project path

# Set the Django settings module (update with your settings module)
os.environ['DJANGO_SETTINGS_MODULE'] = 'ayur_rich.settings'

# Import the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
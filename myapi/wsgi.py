"""
WSGI config for myapi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapi.settings')

application = get_wsgi_application()


# koyeb app init myapi \
#   --git github.com/Vitifolia/quiz-test \
#   --git-branch main \
#   --git-run-command "gunicorn myapi.wsgi" \
#   --ports 8000:http \
#   --routes /:8000 \
#   --env PORT=8000 \
#   --env DJANGO_ALLOWED_HOSTS=myapi-vitifolia.koyeb.app
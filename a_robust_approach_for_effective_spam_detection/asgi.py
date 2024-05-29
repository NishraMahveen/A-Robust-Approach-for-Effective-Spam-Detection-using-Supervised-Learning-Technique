
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'a_robust_approach_for_effective_spam_detection.settings')

application = get_asgi_application()

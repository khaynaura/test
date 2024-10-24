from django.apps import AppConfig
from django.core.management import call_command

class ProductConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "product"

    def ready(self):
        import sys
        if 'runserver' in sys.argv:
            try:
                print("Loading fixture data...")
                call_command('loaddata', 'fixtures/products.json')
            except Exception as e:
                print(f"Error loading fixture: {e}")

#
from django.apps import AppConfig


class LogsConfig(AppConfig):
    """
        Class used to configure the django framework's Logs application. Generating automatically.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    """
        Default model field settings
    """
    name = 'Logs'
    """
        Application name
    """

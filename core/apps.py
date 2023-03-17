from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import core.signals
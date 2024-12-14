from django.apps import AppConfig

class LibonConfig(AppConfig):
    name = 'libon'

    def ready(self):
        import libon.signals 
from django.apps import AppConfig


class AppBlogasConfig(AppConfig):
    name = 'app_blogas'

    def ready(self):
        from .signals import create_profile, save_profile
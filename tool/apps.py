from django.apps import AppConfig
from django.conf import settings


class ToolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tool'

    def ready(self):
        from .models import ToolConfig as PlatformConfig
        from django.db.utils import OperationalError, ProgrammingError

        try:
            if not PlatformConfig.objects.exists():
                PlatformConfig.objects.create(
                    platform="Canvas",
                    issuer=settings.LTI_ISS,
                    jwks_url=settings.LTI_PLATFORM_JWKS_URL,
                    token_url=settings.LTI_ISS + "/login/oauth2/token",
                    client_id=settings.LTI_CLIENT_ID,
                    deployment_id=settings.LTI_DEPLOYMENT_ID,
                )
                print("🟢 Created initial ToolConfig (Canvas).")
        except (OperationalError, ProgrammingError):
            # Happens before migrations
            pass

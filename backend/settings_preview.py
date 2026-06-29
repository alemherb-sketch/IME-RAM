# Local-only settings for previewing the site with `runserver`.
# Production is unaffected (it uses backend.settings on Render).
# We mirror production's DEBUG=False so WhiteNoise serves static/media and
# Django skips the "MEDIA_URL within STATIC_URL" dev check.
from .settings import *  # noqa

DEBUG = False
ALLOWED_HOSTS = ["*"]

# Serve static files straight from the source dirs during preview so CSS/JS/img
# edits show on reload without re-running collectstatic.
WHITENOISE_USE_FINDERS = True
WHITENOISE_AUTOREFRESH = True

# With DEBUG=False Django caches templates in memory; disable that so template
# edits show on reload during local preview (no server restart needed).
for _tpl in TEMPLATES:  # noqa: F405
    if _tpl.get("BACKEND", "").endswith("DjangoTemplates"):
        _tpl["APP_DIRS"] = False
        _tpl.setdefault("OPTIONS", {})["loaders"] = [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ]

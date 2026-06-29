"""Copy committed "seed" media into MEDIA_ROOT (the persistent disk on Render)
without overwriting anything already there.

Why: the catalog/banners shipped in the repo live under static/media/ so they can
be committed. In production MEDIA_ROOT points at a persistent disk (empty on first
boot), so existing image records (products/, services/, banners/) would 404 until
their files are present. This seeds those files once; user uploads are never
touched (we skip files that already exist).

Runs on every start (see render.yaml startCommand); it is idempotent and cheap.
"""
import shutil
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Seed MEDIA_ROOT with the committed media files (idempotent, non-destructive)."
    # Pure filesystem copy; skip system checks so startup is fast and DB-independent.
    requires_system_checks = []

    def handle(self, *args, **options):
        try:
            seed = Path(settings.BASE_DIR) / "static" / "media"
            dest = Path(settings.MEDIA_ROOT)

            if not seed.exists():
                self.stdout.write("seed_media: no seed dir (static/media); nothing to do.")
                return

            if seed.resolve() == dest.resolve():
                self.stdout.write("seed_media: MEDIA_ROOT is the seed dir; nothing to copy.")
                return

            dest.mkdir(parents=True, exist_ok=True)
            copied = 0
            for src in seed.rglob("*"):
                if not src.is_file():
                    continue
                target = dest / src.relative_to(seed)
                if target.exists():
                    continue  # never overwrite (protects user uploads)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, target)
                copied += 1

            self.stdout.write(self.style.SUCCESS(
                f"seed_media: copied {copied} new file(s) into {dest}"))
        except Exception as exc:  # never block app startup on a seeding hiccup
            self.stderr.write(f"seed_media: skipped due to error: {exc}")

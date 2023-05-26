from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(email="admin@admin.com").exists():
            user = User.objects.create(
                email="admin@admin.com",
                username="admin",
                is_superuser=True,
                is_staff=True,
            )
            user.set_password("123456")
            user.save()

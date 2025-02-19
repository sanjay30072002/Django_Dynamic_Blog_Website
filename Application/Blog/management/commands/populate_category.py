from typing import Any
from Blog.models import Post,Category
from django.core.management.base import BaseCommand
import random


class Command(BaseCommand):
    help = "This commands inserts category data"

    def handle(self, *args: Any, **options: Any):
        Category.objects.all().delete()
        
        categories=["Sports","Technology","Art","Food","Science"]



        for category_name in categories:
            Category.objects.create(name=category_name)
            self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))
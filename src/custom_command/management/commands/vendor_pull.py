from django.core.management.base import BaseCommand
import helpers

VENDOR_STATICFILES = {
    "flowbite.min.css":  "https://cdnjs.cloudflare.com/ajax/libs/flowbite/3.4.1/flowbite.min.css",
    "flowbite.min.js": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/3.4.1/flowbite.min.js",

}

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        self.stdout.write("Downloading Vendor Static Files")

        for name, url in VENDOR_STATICFILES.items():
            print(name, url)

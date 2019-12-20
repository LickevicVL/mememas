from django.core.management import BaseCommand
from django.db import models

import memes.models

MODEL_MAPPING = {
    'memes': memes.models
}


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            help='Django application name',
            dest='app_name'
        )
        parser.add_argument(
            help='Model name',
            dest='model_name'
        )

    def handle(self, app_name, model_name, *args, **options):
        try:
            app = MODEL_MAPPING[app_name]
        except KeyError:
            self.stderr.write(
                self.style.ERROR(f'Application \'{app_name}\' not found')
            )

            return

        try:
            model: models.Model = getattr(app, model_name)
        except AttributeError:
            self.stderr.write(
                self.style.ERROR(f'Model \'{model_name}\' does not exist')
            )

            return

        model.objects.all().delete()

        self.stdout.write(
            self.style.SUCCESS(f'{app_name}.models.{model_name} was cleaned')
        )

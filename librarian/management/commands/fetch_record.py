import json
from django.core.management.base import BaseCommand, CommandError

from librarian import primo


class Command(BaseCommand):
    help = 'Fetch one item form primo to stdout'

    def add_arguments(self, parser):
        parser.add_argument('doc_id', type=str)

    def handle(self, *args, **options):
        doc_id = options['doc_id']
        d = primo.primo_request(doc_id)
        json.dump(d, self.stdout, indent=2)

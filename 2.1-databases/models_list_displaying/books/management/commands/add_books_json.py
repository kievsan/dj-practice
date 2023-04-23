import json
from django.core.management.base import BaseCommand
from books.models import Book
from books.converters import DateConverter


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('fixtures/books.json', 'r', encoding='UTF-8') as file:
            books_file = json.load(file)

        for _book in books_file:
            b = Book(
                name=_book['fields']['name'],
                author=_book['fields']['author'],
                pub_date=DateConverter().to_python(_book['fields']['pub_date']),
            )
            b.save()

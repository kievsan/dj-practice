from django.core.management.base import BaseCommand
from books.converters import DateConverter
from books.models import Book


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        books_manual = [
            {'name': 'Сияние',
             'author': 'Стивен Кинг',
             'pub_date': '2018-09-10'
             },
            {'name': '1984',
             'author': 'Джордж Оруэл',
             'pub_date': '2015-03-11'
             },
            {'name': 'Отцы и Дети',
             'author': 'И.С. Тургенев',
             'pub_date': '2015-03-11'
             },
        ]

        for _book in books_manual:
            b = Book(
                name=_book['name'],
                author=_book['author'],
                pub_date=DateConverter().to_python(_book['pub_date']),
            )
            b.save()
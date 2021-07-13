from django.core.management.base import BaseCommand, CommandError
from users.models import Users


class Command(BaseCommand):
    help = 'create test users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help=u'Количество создаваемых пользователей')

    def handle(self, *args, **options):
        total = options['total']
        for el in range(1, total+1):
            try:
                id = Users.objects.order_by('-id')[0].id + 1
            except IndexError:
                id = 1
            Users.objects.create(email=f'test{id}@test.ru')
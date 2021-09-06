from django.core.management.base import BaseCommand

from authapp.models import UserProfile


class Command(BaseCommand):
    def handle(self, *args, **options):
        UserProfile.objects.create_superuser('admin', password='admin')
        UserProfile.objects.create_user('user1', password='password1')
        UserProfile.objects.create_user('user2', password='password2')
        UserProfile.objects.create_user('user3', password='password3')
        UserProfile.objects.create_user('user4', password='password4')
        UserProfile.objects.create_user('user5', password='password5')
        UserProfile.objects.create_user('user6', password='password6')
        UserProfile.objects.create_user('user7', password='password7')
        UserProfile.objects.create_user('user8', password='password8')
        UserProfile.objects.create_user('user9', password='password9')
        UserProfile.objects.create_user('user10', password='password10')
        print('Пользователи созданы!')

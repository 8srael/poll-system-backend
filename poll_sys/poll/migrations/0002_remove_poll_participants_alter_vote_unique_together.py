# Generated by Django 5.1.4 on 2025-03-09 19:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='participants',
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('user', 'poll')},
        ),
    ]

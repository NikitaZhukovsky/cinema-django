# Generated by Django 5.0.3 on 2024-03-10 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producer',
            name='pseudonym',
        ),
        migrations.RemoveField(
            model_name='session',
            name='due_back',
        ),
    ]
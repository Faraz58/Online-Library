# Generated by Django 4.0.3 on 2022-04-09 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_alter_book_inventory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='slug',
        ),
    ]
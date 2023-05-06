# Generated by Django 4.0.3 on 2022-04-03 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_alter_author_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='translators',
            field=models.ManyToManyField(blank=True, related_name='translators', to='library.author'),
        ),
    ]
# Generated by Django 4.2.4 on 2023-09-05 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.TextField(),
        ),
    ]
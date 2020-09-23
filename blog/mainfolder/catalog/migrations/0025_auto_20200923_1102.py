# Generated by Django 3.1.1 on 2020-09-23 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0024_auto_20200923_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='level',
            field=models.IntegerField(choices=[(1, 'Администратор'), (2, 'Модератор'), (3, 'Гость')]),
        ),
    ]

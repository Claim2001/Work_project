# Generated by Django 3.1.1 on 2020-09-22 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_auto_20200919_1843'),
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
            field=models.IntegerField(choices=[(1, 'Администратор'), (3, 'Гость'), (2, 'Модератор')]),
        ),
    ]

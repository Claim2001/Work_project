# Generated by Django 3.1.1 on 2020-09-24 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0027_auto_20200923_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='level',
            field=models.IntegerField(choices=[(1, 'Администратор'), (3, 'Гость'), (2, 'Модератор')]),
        ),
    ]

# Generated by Django 3.1.1 on 2020-09-17 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20200917_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_additional_title',
            field=models.CharField(default=models.CharField(help_text='Название', max_length=200), help_text='Подназвание', max_length=400),
        ),
    ]
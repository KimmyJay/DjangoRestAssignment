# Generated by Django 4.0.5 on 2022-06-22 21:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_article_created_alter_article_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 27, 21, 14, 31, 397266)),
        ),
    ]
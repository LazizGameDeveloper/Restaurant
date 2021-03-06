# Generated by Django 3.2.4 on 2021-08-04 15:34

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_alter_news_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='description',
            field=models.CharField(max_length=200, verbose_name='Подзаголовок'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Содержание'),
        ),
    ]

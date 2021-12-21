# Generated by Django 3.2.4 on 2021-08-04 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210802_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя шефа')),
                ('about', models.CharField(max_length=100, verbose_name='О шефе')),
                ('social_net', models.CharField(max_length=200, verbose_name='Ссылка на соц сеть')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('is_accept', models.BooleanField(default=False, verbose_name='Принят Да/Нет')),
            ],
            options={
                'verbose_name': 'Шеф',
                'verbose_name_plural': 'Шефы',
            },
        ),
    ]
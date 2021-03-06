# Generated by Django 3.2.6 on 2021-08-22 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/default_user.jpg', upload_to='avatars/', verbose_name='Avatar'),
        ),
    ]

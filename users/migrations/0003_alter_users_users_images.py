# Generated by Django 5.0.6 on 2024-06-05 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_users_users_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='users_images',
            field=models.ImageField(blank=True, null=True, upload_to='media/users_profile_images'),
        ),
    ]

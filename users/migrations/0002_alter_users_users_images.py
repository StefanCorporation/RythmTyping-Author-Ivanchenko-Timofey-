# Generated by Django 5.0.6 on 2024-05-28 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='users_images',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
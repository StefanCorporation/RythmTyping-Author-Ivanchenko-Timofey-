# Generated by Django 5.0.6 on 2024-06-03 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_rename_created_add_musicdata_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicdata',
            name='music_type',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
# Generated by Django 4.2.11 on 2024-05-13 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiles',
            old_name='img',
            new_name='image',
        ),
    ]

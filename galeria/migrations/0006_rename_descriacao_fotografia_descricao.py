# Generated by Django 4.2.13 on 2024-08-06 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0005_alter_fotografia_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fotografia',
            old_name='descriacao',
            new_name='descricao',
        ),
    ]
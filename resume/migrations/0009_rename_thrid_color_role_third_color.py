# Generated by Django 4.2.1 on 2023-09-02 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_rename_primary_color_role_first_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='thrid_color',
            new_name='third_color',
        ),
    ]

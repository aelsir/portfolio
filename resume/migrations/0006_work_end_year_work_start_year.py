# Generated by Django 4.2.1 on 2023-09-02 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_remove_project_abb_role_abb'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='end_year',
            field=models.PositiveSmallIntegerField(default=2017),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='start_year',
            field=models.PositiveSmallIntegerField(default=2020),
            preserve_default=False,
        ),
    ]

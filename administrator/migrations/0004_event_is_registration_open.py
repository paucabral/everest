# Generated by Django 3.2.6 on 2021-08-29 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0003_alter_event_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_registration_open',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]

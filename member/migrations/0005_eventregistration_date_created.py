# Generated by Django 3.2.6 on 2021-08-31 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_auto_20210830_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventregistration',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

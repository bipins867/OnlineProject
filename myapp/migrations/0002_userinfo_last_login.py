# Generated by Django 4.2.9 on 2024-01-02 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

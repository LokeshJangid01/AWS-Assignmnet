# Generated by Django 4.0 on 2022-02-17 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='MY POST', max_length=255),
        ),
    ]

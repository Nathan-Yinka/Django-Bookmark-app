# Generated by Django 4.2.4 on 2023-08-17 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='user/%Y/%m/%d/'),
        ),
    ]

# Generated by Django 2.1 on 2019-03-27 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('york', '0008_auto_20190327_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puppyinfo',
            name='profile_image',
            field=models.ImageField(blank=True, default='static/images/default.jpg', null=True, upload_to='static/images'),
        ),
    ]

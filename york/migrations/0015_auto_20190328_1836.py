# Generated by Django 2.1 on 2019-03-28 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('york', '0014_auto_20190328_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puppyinfo',
            name='profile_image',
            field=models.ImageField(default='static/images/default.jpg', upload_to='york/static/images'),
        ),
    ]

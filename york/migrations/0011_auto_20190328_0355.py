# Generated by Django 2.1 on 2019-03-28 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('york', '0010_auto_20190328_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puppyinfo',
            name='profile_image',
            field=models.CharField(blank=True, default='static/images/default.jpg', max_length=2000, null=True),
        ),
    ]

# Generated by Django 2.2.5 on 2019-10-21 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwwards', '0019_auto_20191021_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='avarage',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='creativity',
            field=models.IntegerField(null=True),
        ),
    ]

# Generated by Django 2.2.5 on 2019-10-19 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awwwards', '0009_auto_20191019_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='awwwards.Country'),
        ),
    ]

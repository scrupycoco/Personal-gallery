# Generated by Django 3.0.6 on 2020-05-22 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photolibrary', '0004_auto_20200521_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='image',
            field=models.ImageField(upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='image_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='photolibrary.Location'),
        ),
    ]

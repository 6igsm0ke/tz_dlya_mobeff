# Generated by Django 5.1.5 on 2025-05-18 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_alter_ad_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image_url',
            field=models.URLField(blank=True, max_length=512, null=True),
        ),
    ]

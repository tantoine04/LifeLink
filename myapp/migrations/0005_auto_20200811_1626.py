# Generated by Django 3.0.8 on 2020-08-11 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200811_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='hospital',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

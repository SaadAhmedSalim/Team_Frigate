# Generated by Django 2.1.7 on 2019-12-15 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescription_gen', '0005_auto_20191214_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='tests',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

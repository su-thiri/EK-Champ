# Generated by Django 4.2.11 on 2024-12-07 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EK_APP', '0005_remove_driver_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
# Generated by Django 5.0.2 on 2024-02-16 17:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.color'),
        ),
    ]
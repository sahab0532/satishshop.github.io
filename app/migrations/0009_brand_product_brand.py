# Generated by Django 5.0.2 on 2024-02-16 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_product_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='Brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.brand'),
        ),
    ]
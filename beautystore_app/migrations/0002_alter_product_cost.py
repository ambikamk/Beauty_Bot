# Generated by Django 5.0.4 on 2024-05-15 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautystore_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=10),
        ),
    ]

# Generated by Django 5.0.3 on 2024-05-26 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Forja', '0015_alter_ficha_altura_alter_ficha_falhas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='altura',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='peso',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]

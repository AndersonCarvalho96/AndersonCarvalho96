# Generated by Django 5.0.3 on 2024-05-12 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Forja', '0005_remove_ficha_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficha',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]

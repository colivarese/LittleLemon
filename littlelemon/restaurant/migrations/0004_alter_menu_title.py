# Generated by Django 4.2 on 2023-04-10 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_menu_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]

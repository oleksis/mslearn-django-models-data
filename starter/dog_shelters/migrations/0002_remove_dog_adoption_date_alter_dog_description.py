# Generated by Django 4.0.5 on 2022-06-01 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog_shelters', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='adoption_date',
        ),
        migrations.AlterField(
            model_name='dog',
            name='description',
            field=models.TextField(),
        ),
    ]

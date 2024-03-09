# Generated by Django 3.1.5 on 2023-11-09 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/profiles/', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Фамилия'),
        ),
    ]
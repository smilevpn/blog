# Generated by Django 3.1.5 on 2023-11-02 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preimage',
            field=models.ImageField(default=0, upload_to='static/images/'),
            preserve_default=False,
        ),
    ]
# Generated by Django 2.2.8 on 2019-12-12 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20191212_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='des',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(upload_to='media/images'),
        ),
    ]

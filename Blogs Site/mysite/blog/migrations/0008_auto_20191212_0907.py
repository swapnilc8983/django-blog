# Generated by Django 2.2.8 on 2019-12-12 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20191212_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='des',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=150),
        ),
    ]
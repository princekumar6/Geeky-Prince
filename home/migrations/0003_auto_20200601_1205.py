# Generated by Django 3.0.6 on 2020-06-01 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200601_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=256),
        ),
    ]

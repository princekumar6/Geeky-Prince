# Generated by Django 3.0.6 on 2020-06-01 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=100)),
                ('name', models.TextField()),
            ],
        ),
    ]
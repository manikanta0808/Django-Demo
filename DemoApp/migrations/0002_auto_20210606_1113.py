# Generated by Django 3.2 on 2021-06-06 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DemoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('sid', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=35)),
            ],
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='did',
        ),
    ]

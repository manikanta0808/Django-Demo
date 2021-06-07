# Generated by Django 3.2 on 2021-06-06 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DemoApp', '0003_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='did',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DemoApp.department'),
        ),
        migrations.AddField(
            model_name='students',
            name='year',
            field=models.IntegerField(default=1),
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-04 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='solution_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
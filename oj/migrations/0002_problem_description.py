# Generated by Django 4.0.5 on 2022-07-07 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oj', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='description',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]
# Generated by Django 2.0.3 on 2020-11-22 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='Endclasstclass',
            field=models.CharField(default=2.3, max_length=120),
            preserve_default=False,
        ),
    ]
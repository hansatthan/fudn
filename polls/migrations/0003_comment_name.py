# Generated by Django 2.1.3 on 2018-12-04 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20181204_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='SOME STRING', max_length=50),
        ),
    ]
# Generated by Django 2.0.6 on 2018-11-27 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test_Designing', '0004_auto_20181127_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='time',
            field=models.CharField(max_length=20),
        ),
    ]

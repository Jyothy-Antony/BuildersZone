# Generated by Django 2.1.1 on 2018-09-14 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0034_tbl_requirment'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('workid', models.IntegerField()),
                ('dateofbookng', models.CharField(max_length=100)),
            ],
        ),
    ]

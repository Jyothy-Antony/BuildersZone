# Generated by Django 2.1.1 on 2018-09-22 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0042_delete_tbl_wrkassgn'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_wrkassgn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('reqid', models.IntegerField()),
                ('archid', models.IntegerField()),
                ('startdate', models.CharField(max_length=100)),
                ('enddate', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]

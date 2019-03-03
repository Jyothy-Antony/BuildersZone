# Generated by Django 2.1.1 on 2018-09-12 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0025_delete_tbl_garden'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_garden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.CharField(max_length=1000)),
                ('location', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='file')),
                ('userid', models.IntegerField()),
                ('companyid', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 2.1.1 on 2018-09-04 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0008_tbl_addwork'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_addprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('features', models.CharField(max_length=10000)),
                ('works', models.CharField(max_length=100)),
                ('wrkimg', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='file')),
            ],
        ),
    ]

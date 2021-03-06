# Generated by Django 2.1.1 on 2018-09-03 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_delete_tbl_addwork'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_addwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_name', models.CharField(max_length=100)),
                ('add_place', models.CharField(max_length=100)),
                ('add_prize', models.CharField(max_length=100)),
                ('add_sqrft', models.CharField(max_length=100)),
                ('add_typ', models.CharField(max_length=100)),
                ('add_image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='file')),
                ('add_nearby', models.CharField(max_length=100)),
                ('add_des', models.CharField(max_length=10000)),
                ('add_bedrooms', models.CharField(max_length=100)),
                ('add_toilet', models.CharField(max_length=100)),
                ('add_floor', models.CharField(max_length=100)),
            ],
        ),
    ]

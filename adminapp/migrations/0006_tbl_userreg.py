# Generated by Django 2.1.1 on 2018-09-03 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_delete_tbl_userreg'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_userreg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_name', models.CharField(max_length=100)),
                ('add_address', models.CharField(max_length=100)),
                ('add_email', models.CharField(max_length=100)),
                ('add_phone', models.CharField(max_length=100)),
                ('add_place', models.CharField(max_length=100)),
                ('add_approve', models.CharField(max_length=100)),
                ('add_pas', models.CharField(max_length=100)),
                ('add_lic', models.CharField(max_length=100)),
                ('add_image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='file')),
                ('add_type', models.CharField(max_length=100)),
                ('add_desc', models.CharField(max_length=10000)),
            ],
        ),
    ]

# Generated by Django 2.1.1 on 2018-09-22 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0044_remove_tbl_wrkassgn_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_payment',
        ),
    ]
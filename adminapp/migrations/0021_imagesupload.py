# Generated by Django 2.1.1 on 2018-09-06 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0020_delete_imagesupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='imagesupload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reqid', models.IntegerField()),
                ('imag', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='file')),
                ('cost', models.CharField(max_length=100)),
            ],
        ),
    ]

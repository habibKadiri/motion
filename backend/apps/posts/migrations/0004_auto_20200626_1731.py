# Generated by Django 3.0.3 on 2020-06-26 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200626_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, default=list, null=True, upload_to=''),
        ),
    ]

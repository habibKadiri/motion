# Generated by Django 3.0.3 on 2020-06-25 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200625_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='shared',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.Post'),
        ),
    ]

# Generated by Django 3.0.3 on 2020-06-25 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0001_initial'),
        ('comments', '0004_auto_20200625_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_comments', to='userprofiles.UserProfile', verbose_name='user'),
        ),
    ]

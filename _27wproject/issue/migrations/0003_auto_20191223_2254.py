# Generated by Django 2.2.4 on 2019-12-23 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0002_auto_20191026_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuecomment',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issue.Issue'),
        ),
    ]

# Generated by Django 2.1.3 on 2018-11-29 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0007_auto_20181129_0747'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='test2',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
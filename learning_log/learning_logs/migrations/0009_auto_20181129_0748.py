# Generated by Django 2.1.3 on 2018-11-29 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0008_testmodel_test2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gtest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='TestModel',
        ),
    ]

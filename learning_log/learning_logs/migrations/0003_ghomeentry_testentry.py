# Generated by Django 2.1.3 on 2018-11-28 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ghomeentry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=500)),
                ('userName', models.CharField(max_length=50)),
                ('typeName', models.CharField(max_length=50)),
                ('date_public', models.DateTimeField(auto_now_add=True)),
                ('read_num', models.IntegerField(max_length=200)),
                ('imageName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Testentry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=500)),
                ('userName', models.CharField(max_length=50)),
                ('typeName', models.CharField(max_length=50)),
                ('date_public', models.DateTimeField(auto_now_add=True)),
                ('read_num', models.IntegerField(max_length=200)),
                ('imageName', models.CharField(max_length=50)),
            ],
        ),
    ]
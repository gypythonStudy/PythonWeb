# Generated by Django 2.1.3 on 2018-11-29 07:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0009_auto_20181129_0748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('content', models.TextField(default='', verbose_name='正文')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击量')),
                ('imageName', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '我的博客',
                'verbose_name_plural': '我的博客',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='博客类别')),
                ('number', models.IntegerField(default=1, verbose_name='分类数目')),
            ],
            options={
                'verbose_name': '博客类别',
                'verbose_name_plural': '博客类别',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='佚名', max_length=20, verbose_name='姓名')),
                ('content', models.CharField(max_length=300, verbose_name='内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_logs.Blog', verbose_name='博客')),
            ],
            options={
                'verbose_name': '博客评论',
                'verbose_name_plural': '博客评论',
            },
        ),
        migrations.CreateModel(
            name='Counts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_nums', models.IntegerField(default=0, verbose_name='博客数目')),
                ('category_nums', models.IntegerField(default=0, verbose_name='分类数目')),
                ('tag_nums', models.IntegerField(default=0, verbose_name='标签数目')),
                ('visit_nums', models.IntegerField(default=0, verbose_name='网站访问量')),
            ],
            options={
                'verbose_name': '数目统计',
                'verbose_name_plural': '数目统计',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='博客标签')),
                ('number', models.IntegerField(default=1, verbose_name='标签数目')),
            ],
            options={
                'verbose_name': '博客标签',
                'verbose_name_plural': '博客标签',
            },
        ),
        migrations.DeleteModel(
            name='Gtest',
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_logs.Category', verbose_name='博客类别'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(to='learning_logs.Tag', verbose_name='博客标签'),
        ),
    ]

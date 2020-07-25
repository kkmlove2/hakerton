# Generated by Django 3.0.8 on 2020-07-25 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('time', models.DateTimeField()),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.Blog')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentbody', models.CharField(max_length=30)),
                ('time', models.DateTimeField()),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Blog')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='hashtags',
            field=models.ManyToManyField(blank=True, to='post.Hashtag'),
        ),
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.ManyToManyField(related_name='likes', through='post.Like', to=settings.AUTH_USER_MODEL),
        ),
    ]
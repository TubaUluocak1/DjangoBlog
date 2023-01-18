# Generated by Django 4.1 on 2022-12-05 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_alter_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('subtitle', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
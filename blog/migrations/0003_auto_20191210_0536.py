# Generated by Django 2.2.7 on 2019-12-10 05:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20191210_0522'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllBlogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('like_num', models.IntegerField()),
                ('blogger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
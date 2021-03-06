# Generated by Django 3.0.6 on 2020-06-05 08:14

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_blogas', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='blog_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment', to='app_blogas.Field'),
        ),
        migrations.AlterField(
            model_name='field',
            name='author',
            field=models.CharField(max_length=50, null=True, verbose_name=django.contrib.auth.models.User),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-28 07:59

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True, verbose_name='Pavadinimas')),
                ('time', models.DateTimeField(null=True, verbose_name='Sukurta')),
                ('text', tinymce.models.HTMLField(max_length=500, null=True, verbose_name='Tekstas')),
                ('author', models.CharField(max_length=50, null=True, verbose_name='Author')),
            ],
        ),
    ]

# Generated by Django 5.2.1 on 2025-05-28 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RESUME',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('summary', models.TextField()),
                ('education', models.TextField()),
                ('exprience', models.TextField()),
                ('skills', models.CharField(max_length=250)),
            ],
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-30 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0002_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
            ],
        ),
    ]

# Generated by Django 4.1.5 on 2023-05-31 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('fb_link', models.URLField(max_length=100)),
                ('twi_link', models.URLField(max_length=100)),
                ('goo_link', models.URLField(max_length=100)),
            ],
        ),
    ]

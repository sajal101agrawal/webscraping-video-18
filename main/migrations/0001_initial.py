# Generated by Django 4.2.6 on 2023-10-11 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='videos_collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Video_name', models.CharField(blank=True, max_length=255, null=True)),
                ('Release_Date', models.DateTimeField(blank=True, null=True)),
                ('Poster_Image_uri', models.URLField(blank=True, null=True)),
                ('Likes', models.IntegerField(blank=True, null=True)),
                ('Disclike', models.IntegerField(blank=True, null=True)),
                ('Url', models.URLField(blank=True, null=True)),
                ('Title', models.CharField(max_length=255)),
                ('Discription', models.TextField(blank=True, null=True)),
                ('Pornstarts', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]

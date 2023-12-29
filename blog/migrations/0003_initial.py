# Generated by Django 5.0 on 2023-12-24 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0002_delete_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('auther', models.CharField(max_length=13)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
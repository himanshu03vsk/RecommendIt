# Generated by Django 3.1.4 on 2020-12-17 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50)),
                ('Release_year', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
                ('cast', models.CharField(max_length=40)),
            ],
        ),
    ]

# Generated by Django 3.0.6 on 2020-07-12 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('lat', models.CharField(max_length=20)),
                ('lon', models.CharField(max_length=20)),
                ('near', models.CharField(max_length=50)),
                ('sug', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=225)),
            ],
            options={
                'db_table': 'collect',
            },
        ),
    ]

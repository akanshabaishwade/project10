# Generated by Django 4.0 on 2021-12-29 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picnic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=30)),
                ('student_class', models.CharField(max_length=4)),
                ('student_fee', models.IntegerField()),
            ],
        ),
    ]

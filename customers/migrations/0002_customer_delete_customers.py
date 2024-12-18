# Generated by Django 5.1.3 on 2024-11-19 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=40)),
                ('gender', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Customers',
        ),
    ]

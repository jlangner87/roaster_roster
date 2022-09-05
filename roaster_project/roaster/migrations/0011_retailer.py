# Generated by Django 4.1 on 2022-09-05 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roaster', '0010_delete_retailer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Retailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('address_line2', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
            ],
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-06 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('profile_pic', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Roaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=20)),
                ('bio', models.CharField(blank=True, max_length=2000)),
                ('site_url', models.CharField(max_length=200)),
                ('display_pic', models.CharField(blank=True, max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roaster', to='icdb2.user')),
            ],
        ),
        migrations.CreateModel(
            name='Bean',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('origin', models.CharField(max_length=100)),
                ('bean_type', models.CharField(blank=True, max_length=100)),
                ('roast_type', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2000)),
                ('organic', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('buy_url', models.CharField(max_length=200)),
                ('product_pic', models.CharField(blank=True, max_length=200)),
                ('roaster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beans_list', to='icdb2.roaster')),
            ],
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-06 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('icdb2', '0002_alter_bean_roaster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roaster',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roaster', to='icdb2.user'),
        ),
    ]
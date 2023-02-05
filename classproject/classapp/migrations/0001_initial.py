# Generated by Django 4.1.4 on 2023-01-31 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fooditem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Foodname', models.CharField(max_length=100)),
                ('Foodprice', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('Username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Useraddress', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rating', models.IntegerField()),
                ('Foodid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Foodsid', to='classapp.fooditem')),
                ('Reviewername', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='username', to='classapp.user')),
            ],
        ),
    ]
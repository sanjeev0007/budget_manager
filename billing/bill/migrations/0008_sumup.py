# Generated by Django 2.2.2 on 2019-08-16 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0007_budget_month'),
    ]

    operations = [
        migrations.CreateModel(
            name='sumup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('total', models.IntegerField(default=0)),
                ('month', models.CharField(default=8, max_length=2)),
            ],
        ),
    ]

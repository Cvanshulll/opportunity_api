# Generated by Django 4.1.5 on 2023-01-15 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('opportunity_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('role', models.TextField()),
                ('batch', models.CharField(max_length=100)),
                ('job_id', models.CharField(max_length=100)),
                ('job_link', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('end_date', models.DateField(blank=True, default='')),
                ('description', models.TextField()),
                ('stipend', models.CharField(max_length=100)),
                ('added_date', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]

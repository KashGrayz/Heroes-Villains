# Generated by Django 4.1.3 on 2022-11-15 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0003_rename_type_super_super_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]

# Generated by Django 4.1.3 on 2024-01-15 17:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blogs/')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=200)),
                ('publication_date', models.DateField(default=datetime.date.today)),
                ('categories', models.CharField(choices=[('marketi', 'Marketi'), ('aplikacia', 'Aplikacia'), ('xelovnuri_inteleqti', 'Xelovnuri Inteleqti'), ('UI_UX', 'UI/UX'), ('kvleva', 'Kvleva'), ('Figma', 'Figma')], max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]

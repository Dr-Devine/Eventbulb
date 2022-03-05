# Generated by Django 3.2.6 on 2021-08-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('datetime', models.DateTimeField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]

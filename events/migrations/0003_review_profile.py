# Generated by Django 4.0.2 on 2022-03-22 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_attending'),
        ('events', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='profile',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='accounts.userprofile'),
            preserve_default=False,
        ),
    ]

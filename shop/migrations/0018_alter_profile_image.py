# Generated by Django 5.0.4 on 2024-05-02 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_remove_profile_photo_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='profiles'),
        ),
    ]
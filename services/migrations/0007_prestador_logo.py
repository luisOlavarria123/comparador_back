# Generated by Django 5.0.3 on 2024-10-31 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_rename_review_resenia'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestador',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='prestadores/'),
        ),
    ]

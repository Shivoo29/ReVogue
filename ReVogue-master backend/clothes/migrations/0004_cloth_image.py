# Generated by Django 4.1.4 on 2023-10-14 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0003_cloth_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloth',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-25 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyUniversity', '0003_auto_20201026_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=256),
        ),
    ]

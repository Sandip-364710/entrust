# Generated by Django 5.0.3 on 2024-03-30 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employ',
            name='email',
            field=models.EmailField(default='exit', max_length=254),
            preserve_default=False,
        ),
    ]
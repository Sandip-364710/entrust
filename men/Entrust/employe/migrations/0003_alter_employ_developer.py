# Generated by Django 5.0.3 on 2024-07-24 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0002_employ_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employ',
            name='developer',
            field=models.CharField(choices=[('frontend Developer', 'frontend Developer'), ('backend Developer', 'backend Developer'), ('java Developer', 'java Developer'), ('Python Developer', 'Python Developer'), ('php Developer', 'php Developer'), ('graphic designer', 'graphic designer'), ('fullstack Developer', 'fullstack Developer'), ('Technical Leader', 'Technical Leader'), ('Associate Software Engineer', 'Associate Software Engineer'), ('Consulting python Developer', 'Consulting python Developer'), ('Junior Software Engineer', 'Junior Software Engineer'), ('Senior Ui/Ux Designer', 'Senior Ui/Ux Designer'), ('Technical Director', 'Technical Director')], max_length=50),
        ),
    ]
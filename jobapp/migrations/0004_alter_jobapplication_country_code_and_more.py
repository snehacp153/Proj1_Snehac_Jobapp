# Generated by Django 4.2.5 on 2023-10-20 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0003_rename_country_code_jobapplication_country_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='country_code',
            field=models.CharField(choices=[('', '+91'), ('india', '+91'), ('canada', '+1')], max_length=20),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='experience_month',
            field=models.CharField(choices=[('', 'months'), ('0month', '0 month'), ('1month', '1 month'), ('2month', '2 month'), ('3month', '3 month'), ('4month', '4 month'), ('5month', '5 month')], max_length=6),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='phone_no',
            field=models.CharField(max_length=20),
        ),
    ]

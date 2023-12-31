# Generated by Django 4.2.5 on 2023-10-20 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0002_alter_jobapplication_phone_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobapplication',
            old_name='Country_code',
            new_name='country_code',
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='experience_year',
            field=models.CharField(choices=[('', 'years'), ('fresher', 'fresher'), ('1year', '1 year'), ('2year', '2 year'), ('3year', '3 year'), ('4plusyear', '4+ year')], max_length=9),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='job_role',
            field=models.CharField(choices=[('', 'Choose a Job Role'), ('frontenddeveloper', 'Frontend Developer'), ('backenddeveloper', 'Backend Developer'), ('fullstackdeveloper', 'Fullstack Developer'), ('frontenddeveloper', 'Frontend Developer'), ('uiuxdeveloper', 'Ui/UX Designer')], max_length=19),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='qualification',
            field=models.CharField(choices=[('', 'Course'), ('bca', 'BCA'), ('btech', 'Btech'), ('mca', 'MCA'), ('mtech', 'Mtech')], max_length=5),
        ),
    ]

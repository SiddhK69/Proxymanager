# Generated by Django 4.0.4 on 2022-10-02 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_sub_timetable42_teacher_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='Table_Id',
            field=models.IntegerField(default=1),
        ),
    ]
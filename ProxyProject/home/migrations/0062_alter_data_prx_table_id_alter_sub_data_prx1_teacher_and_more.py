# Generated by Django 4.1 on 2023-05-22 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0061_alter_data_prx_table_id_alter_sub_data_prx1_teacher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_prx',
            name='Table_Id',
            field=models.CharField(default=6, max_length=2, unique=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx1',
            name='Teacher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.data_prx'),
        ),
        migrations.AlterField(
            model_name='sub_data_prx10',
            name='Teacher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.data_prx'),
        ),
        migrations.AlterField(
            model_name='sub_data_prx11',
            name='Teacher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.data_prx'),
        ),
        migrations.AlterField(
            model_name='sub_data_prx2',
            name='Teacher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.data_prx'),
        ),
        migrations.AlterField(
            model_name='sub_data_prx3',
            name='Teacher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.data_prx'),
        ),
        migrations.AlterField(
            model_name='sub_data_prx4',
            name='Teacher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.data_prx'),
        ),
        migrations.AlterField(
            model_name='sub_data_prx5',
            name='Teacher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.data_prx'),
        ),
        migrations.AlterField(
            model_name='sub_data_prx6',
            name='Teacher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.data_prx'),
        ),
        migrations.AlterField(
            model_name='sub_data_prx7',
            name='Teacher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.data_prx'),
        ),
        migrations.AlterField(
            model_name='sub_data_prx8',
            name='Teacher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.data_prx'),
        ),
        migrations.AlterField(
            model_name='sub_data_prx9',
            name='Teacher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.data_prx'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='Table_Id',
            field=models.CharField(default=31, max_length=2, unique=True),
        ),
    ]
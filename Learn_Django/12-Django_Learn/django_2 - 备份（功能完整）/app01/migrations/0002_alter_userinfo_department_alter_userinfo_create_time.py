# Generated by Django 4.1 on 2022-09-08 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='Department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.department', verbose_name='所属部门'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='create_time',
            field=models.DateField(verbose_name='入职时间'),
        ),
    ]

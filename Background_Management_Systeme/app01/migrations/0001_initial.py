# Generated by Django 4.1 on 2022-09-16 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='管理员姓名')),
                ('password', models.CharField(max_length=64, verbose_name='管理员密码')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='标题')),
            ],
        ),
        migrations.CreateModel(
            name='PrettyNum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机号')),
                ('price', models.IntegerField(verbose_name='价格')),
                ('level', models.SmallIntegerField(choices=[(1, '一级'), (2, '二级'), (3, '三级'), (4, '四级')], default=1, verbose_name='级别')),
                ('status', models.SmallIntegerField(choices=[(1, '已占用'), (2, '未占用')], default=2, verbose_name='状态')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='姓名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('account_balance', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='账户余额')),
                ('create_time', models.DateField(verbose_name='入职时间')),
                ('gender', models.SmallIntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别')),
                ('user_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.department', verbose_name='员工所属部门')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.SmallIntegerField(choices=[(1, '紧急'), (2, '重要'), (3, '常规')], default=3, verbose_name='任务级别')),
                ('task_title', models.CharField(max_length=64, verbose_name='任务标题')),
                ('task_content', models.TextField(verbose_name='任务内容')),
                ('Person_in_Charge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.admin', verbose_name='负责人')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oid', models.CharField(max_length=64, verbose_name='订单号')),
                ('name', models.CharField(max_length=32, verbose_name='订单名称')),
                ('price', models.IntegerField(verbose_name='价格')),
                ('status', models.SmallIntegerField(choices=[(1, '待支付'), (2, '已支付')], default=1, verbose_name='状态')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.admin', verbose_name='管理员')),
            ],
        ),
    ]

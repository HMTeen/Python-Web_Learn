from django.db import models



# Create your models here.
class Department(models.Model):
    # 部门表
    title = models.CharField(verbose_name='标题', max_length=32)
    
    # 实例化对象打印的时候，就展示输出self.title的内容
    def __str__(self):
        return self.title

class UserInfo(models.Model):
    # 部门表
    name = models.CharField(verbose_name='姓名', max_length=16)
    password = models.CharField(verbose_name='密码', max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账户余额',
                                  max_digits=10, 
                                  decimal_places=2,
                                  default=0)
    create_time = models.DateField(verbose_name='入职时间')
    
    # # 无约束创建
    # Department_id = models.BigIntegerField(verbose_name='部门ID')
    
    # 有约束创建
    # 和Department表格的id关联，只能是里面的id，才能合格创建
    # ! 创建的Department会自动变为：Department_id
    # 级联删除
    Department = models.ForeignKey(verbose_name='所属部门', to="Department", to_field="id",
                                   on_delete = models.CASCADE)

    # # 信息置空
    # Department = models.ForeignKey(to="Department", to_field="id",
    #                                on_delete = models.SET_NULL)
    gender_choices = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
    
    
class PrettyNum(models.Model):
    ''' 靓号管理'''
    # 默认有自增id
    mobile = models.CharField(verbose_name='手机号', max_length=11)
    price = models.IntegerField(verbose_name='价格')
    level_choices = (
        (1, '一级'),
        (2, '二级'),
        (3, '三级'),
        (4, '四级')
    )
    level = models.SmallIntegerField(verbose_name='级别', choices=level_choices, default=1)
    
    status_choices = (
        (1, '已占用'),
        (2, '未占用')
    )
    status = models.SmallIntegerField(verbose_name='状态', choices=status_choices, default=2)
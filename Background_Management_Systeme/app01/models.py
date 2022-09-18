from django.db import models

# Create your models here.

# 创建管理员数据表
class Admin(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    # 关联表格页面展示问题：定义str函数，即可解决输出为object对象的问题
    def __str__(self):
        return self.name
        
        
# 创建部门数据表
class Department(models.Model):
    name = models.CharField(verbose_name='部门名称', max_length=32)
    
    # 实例化对象打印的时候，就展示输出self.title的内容
    def __str__(self):
        return self.name


# 创建用户数据表
class UserInfo(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=16)
    password = models.CharField(verbose_name='密码', max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    account_balance = models.DecimalField(verbose_name='账户余额',
                                          max_digits=10, 
                                          decimal_places=2,
                                          default=0)
    create_time = models.DateField(verbose_name='入职时间')
    user_department = models.ForeignKey(verbose_name='员工所属部门', to="Department", to_field="id",
                                        on_delete = models.CASCADE)

    gender_choices = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)



# 创建靓号数据表
class PrettyNum(models.Model):
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
    

# 创建任务类数据表
class Task(models.Model):
    level_choices = (
        (1, '紧急'),
        (2, '重要'),
        (3, '常规'),
    )
    level = models.SmallIntegerField(verbose_name='任务级别', choices=level_choices, default=3)
    task_title = models.CharField(verbose_name='任务标题', max_length=64)
    task_content = models.TextField(verbose_name='任务内容')
    Person_in_Charge = models.ForeignKey(verbose_name='负责人', to='Admin', on_delete=models.CASCADE)
    

# 订单设计
class Order(models.Model):
    oid = models.CharField(verbose_name='订单号', max_length=64)
    name = models.CharField(verbose_name='订单名称', max_length=32)
    price = models.IntegerField(verbose_name='价格')
    
    status_choices = (
        (1, '待支付'),
        (2, '已支付'),
    )
    status = models.SmallIntegerField(verbose_name='状态', choices=status_choices, default=1)
    
    # 本该跟用户关联，用户数据太多，就先跟管理员关联
    admin = models.ForeignKey(verbose_name='管理员', to='Admin', on_delete=models.CASCADE)
    
    
    
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField()
    
# !上述定义python类等价于：
'''
create table app01_userinfo(                # table名字：app01_类名小写
	id bigint auto_increment primary key,   # django自动添加
    name varchar(32),
    password varchar(32),
	age int
)default charset=utf8;
'''

# !操作数据表中的数据【仅展示，不会写在这里】
'''
# 等价于 insert into app01_userinfo(name, password, age) values('gsf', 'pwd', '20')
UserInfo.objects.create(name='gsf', password='pwd', age='20')
'''
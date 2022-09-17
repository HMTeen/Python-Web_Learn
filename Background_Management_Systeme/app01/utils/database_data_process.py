from app01 import models
import random
from app01.utils.Encrypts import *

class Data_Create():
    def __init__(self):
        self.create_data_num = 50
    
    def Department(self):    
        for i in range(self.create_data_num):
            models.Department.objects.create(name='部门-test-'+ str(i))
            
            
    def UserInfo(self):    
        for i in range(self.create_data_num):
            # 若使用外键（关联有表格），就要这样提交，例：Derpartment
            user_department = models.Department.objects.get(id=i%2+2)
            models.UserInfo.objects.create(name='gs'+str(i), 
                                           password='jkl'+str(i), 
                                           age=i+5, 
                                           account_balance=i+800,
                                           create_time='2022-11-12',
                                           gender=i%2+1,
                                           user_department=user_department)
            
    def PrettyNum(self):    
        for i in range(10, self.create_data_num):
            # 若使用外键（关联有表格），就要这样提交，例：Derpartment
            models.PrettyNum.objects.create(mobile='157375932'+str(i),
                                            price = 7777 + i,
                                            level=random.randint(1, 4),
                                            status=random.randint(1, 2))

    def admin(self):
        for i in range(self.create_data_num):
            models.Admin.objects.create(name='gs'+str(i),
                                        password=md5('12'+str(i)))
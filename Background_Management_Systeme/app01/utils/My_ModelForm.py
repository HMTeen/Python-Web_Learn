from django import forms
from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from app01.utils.Encrypts import *

# ！ 定义BootStrap样式父类
class BootStrap_ModelForm_Parent(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        for name, field in self.fields.items():
            field.widget.attrs['class'] = "form-control"
            if name == 'create_time':
                field.widget.attrs['placeholder'] = '请输入' + field.label + '【例：2022-01-21】' 
                
            elif name == 'confirm_password':
                field.widget.attrs['placeholder'] = '请' + field.label
                            
            else:
                field.widget.attrs['placeholder'] = '请输入' + field.label 


# ！ 管理员类
class AdminModelForm_list(BootStrap_ModelForm_Parent):
    class Meta:
        model = models.Admin
        fields = '__all__'

class AdminModelForm_add(BootStrap_ModelForm_Parent):
    
    # 想添加一个确认密码的按钮
    confirm_password = forms.CharField(label='确认管理员密码',
                                       widget=forms.PasswordInput)
    
    class Meta:
        model = models.Admin
        fields = '__all__'
        
        widgets = {
            'password':forms.PasswordInput(render_value=True)}
    
    # 钩子函数
    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)
    
    def clean_confirm_password(self):
        confirm_password = md5(self.cleaned_data.get('confirm_password'))
        # 密码不用再加密了，已经加密过一次了
        password = self.cleaned_data.get('password')
        if password != confirm_password:
            raise ValidationError('密码不一致')
        
        # 返回什么，数据库到时候就保存什么
        return confirm_password

class AdminModelForm_edit(BootStrap_ModelForm_Parent):
    
    # 想添加一个确认密码的按钮
    confirm_password = forms.CharField(label='确认管理员密码',
                                       widget=forms.PasswordInput)
    
    # disabled=True  设置输入框内容不可修改
    password = forms.CharField(label='管理员密码')
    name = forms.CharField(label='管理员名字', disabled=True)
    
    class Meta:
        model = models.Admin
        fields = '__all__'
        
        widgets = {
            'password':forms.PasswordInput(render_value=True)
        }
    
    # def clean_password(self):
    #     pwd = self.cleaned_data.get('password')
    #     return md5(pwd)
    
    def clean_confirm_password(self):
        confirm_password = md5(self.cleaned_data.get('confirm_password'))
        # 密码不用再加密了，已经加密过一次了
        password = self.cleaned_data.get('password')
        if password != confirm_password:
            raise ValidationError('密码不一致')
        
        # 返回什么，数据库到时候就保存什么
        return confirm_password
    
class AdminModelForm_reset(BootStrap_ModelForm_Parent):
    
    name = forms.CharField(label='管理员姓名', disabled=True)
    confirm_password = forms.CharField(label='确认管理员密码',
                                       widget=forms.PasswordInput)
 
    class Meta:
        model = models.Admin
        fields = '__all__'
        
        widgets = {
            'password':forms.PasswordInput(render_value=True)
        }
    
    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        pwd_new = md5(pwd)
        
        # 去数据库校验：修改的密码是否和以前一样
        if models.Admin.objects.filter(id=self.instance.pk, password=pwd_new).exists():
            raise ValidationError('新密码不能和原密码一致')
        
        return pwd_new
    
    def clean_confirm_password(self):
        confirm_password = md5(self.cleaned_data.get('confirm_password'))
        # 密码不用再加密了，已经加密过一次了
        password = self.cleaned_data.get('password')
        if password != confirm_password:
            raise ValidationError('密码不一致')
        
        # 返回什么，数据库到时候就保存什么
        return confirm_password


# ！ Department类
class DepartmentModelForm_list(BootStrap_ModelForm_Parent):
    class Meta:
        model = models.Department
        fields = '__all__'

class DepartmentModelForm_add(BootStrap_ModelForm_Parent):
    class Meta:
        model = models.Department
        fields = '__all__'
        
class DepartmentModelForm_edit(BootStrap_ModelForm_Parent):
    class Meta:
        model = models.Department
        fields = '__all__'
        

# ！ user类
class UserModelForm_list(BootStrap_ModelForm_Parent):
    class Meta:
        model = models.UserInfo
        fields = '__all__'

class UserModelForm_add(BootStrap_ModelForm_Parent):
    # 添加校验规则
    name = forms.CharField(min_length=2, label='姓名')
    class Meta:
        model = models.UserInfo
        fields = '__all__'

class UserModelForm_edit(BootStrap_ModelForm_Parent):
    class Meta:
        model = models.UserInfo
        fields = '__all__'


# ！ 靓号类
class PrettynumModelForm_list(BootStrap_ModelForm_Parent):
    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']

class PrettynumModelForm_add(BootStrap_ModelForm_Parent):
    
    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']

    # @ 验证方法2：定义字段函数
    def clean_mobile(self):
        text_mobile = self.cleaned_data['mobile']
        
        if len(text_mobile) != 11:
            raise ValidationError('手机号长度错误')
        
        if models.PrettyNum.objects.filter(mobile=text_mobile).exists():
           raise ValidationError('手机号已存在') 
        return text_mobile
    
class PrettynumModelForm_edit(BootStrap_ModelForm_Parent):

    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']
    
    # @ 验证方法2：定义字段函数
    def clean_mobile(self):
        text_mobile = self.cleaned_data['mobile']
        # 获取当前编辑行数据的id
        id_mobile = self.instance.pk
        
        if len(text_mobile) != 11:
            raise ValidationError('手机号长度错误')
        
        if models.PrettyNum.objects.filter(mobile=text_mobile).exclude(id=id_mobile).exists():
           raise ValidationError('手机号已存在') 
        return text_mobile
    
    
# ！ 任务类
class TaskModelForm_list(BootStrap_ModelForm_Parent):
    class Meta:
        model = models.Task
        fields = '__all__'

class TaskModelForm_add(BootStrap_ModelForm_Parent):
    class Meta:
        model = models.Task
        fields = '__all__'
        
class TaskModelForm_edit(BootStrap_ModelForm_Parent):
    class Meta:
        model = models.Task
        fields = '__all__'
        

# ！ 订单类
class OrderModelForm_list(BootStrap_ModelForm_Parent):
    class Meta:
        model = models.Order
        fields = '__all__'
        
class OrderModelForm_add(BootStrap_ModelForm_Parent):
    class Meta:
        model = models.Order
        # fields = '__all__'
        exclude = ['oid', 'admin']
        
class OrderModelForm_edit(BootStrap_ModelForm_Parent):
    class Meta:
        model = models.Order
        # fields = '__all__'
        exclude = ['oid', 'admin']
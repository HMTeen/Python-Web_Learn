from django import forms
from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from app01.utils.Encrypts import *

# 定于BootStrap_Form父类
class BootStrap_Form(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
 
            if field.widget.attrs:
                field.widget.attrs['class'] = "form-control"
                field.widget.attrs['placeholder'] = '请输入' + field.label
            else:
                field.widget.attrs = {'class':"form-control",
                                      'placeholder':'请输入' + field.label
                    }


# ！ user类
# Form组件-user_add
class UserForm_add(BootStrap_Form):
    
    name = forms.CharField(label='名字')
    password = forms.CharField(label='密码')
    age = forms.IntegerField(label='年龄')
    account = forms.DecimalField(label='账户余额')
    create_time = forms.DateField(label='创建时间')
    Department = forms.CharField(label='所属部门')
    gender = forms.CharField(label='性别')
    
    

# ！ login类
class LoginForm(BootStrap_Form):
    name = forms.CharField(label='用户名',
                           widget=forms.TextInput)
                           
    password = forms.CharField(label='密码',
                               widget=forms.PasswordInput(render_value=True))
    
    code = forms.CharField(label='图片验证码',
                           widget=forms.TextInput)
    
    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        
        return md5(pwd)
        
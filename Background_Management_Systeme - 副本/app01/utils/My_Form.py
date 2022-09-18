from django import forms
from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from app01.utils.Encrypts import *

# 定于BootStrap_Form_Parent父类
class BootStrap_Form_Parent(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if field.widget.attrs:
                field.widget.attrs['class'] = "form-control"
                field.widget.attrs['placeholder'] = '请输入' + field.label
            else:
                field.widget.attrs = {'class':"form-control",
                                      'placeholder':'请输入' + field.label}


# ！ 用户登录
class LoginForm(BootStrap_Form_Parent):
    name = forms.CharField(label='用户名',
                           widget=forms.TextInput)
                           
    password = forms.CharField(label='密码',
                               widget=forms.PasswordInput(render_value=True))
    
    code = forms.CharField(label='图片验证码',
                           widget=forms.TextInput)
    
    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)
        
from django import forms
from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Form组件-user_add
class UserForm_add(forms.Form):
    name = forms.CharField(label='名字')
    password = forms.CharField(label='密码')
    age = forms.IntegerField(label='年龄')
    account = forms.DecimalField(label='账户余额')
    create_time = forms.DateField(label='创建时间')
    Department = forms.CharField(label='所属部门')
    gender = forms.CharField(label='性别')
    

# ModelForm组件-user_add
class UserModelForm_add(forms.ModelForm):
    
    # ！在此添加更多校验规则
    name = forms.CharField(min_length=2, label='姓名')
    
    class Meta:
        model = models.UserInfo
        # fields = ['name', 'password', 'age', 'account', 'create_time', 'gender', 'Department']
        fields = '__all__'
        
        # ！手动更改输入框样式
        # widgets = {
        #     'name':forms.TextInput( attrs={'class':"form-control"} ),
        # }
        
    # ！自动更改输入框样式
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            if name == 'create_time':
                field.widget.attrs = {'class':"form-control", 
                                  'placeholder': '请输入' + field.label + '【例：2022-01-21】'}
            else:
                field.widget.attrs = {'class':"form-control", 
                                      'placeholder':'请输入' + field.label}
                


class PrettynumAddModelForm_add(forms.ModelForm):
    
    # # @ 验证方法1：添加手机号校验规则
    # mobile = forms.CharField(
    #     label="手机号",
    #     validators = [RegexValidator(r'^1(3[0-9]|4[01456879]|5[0-35-9]|6[2567]|7[0-8]|8[0-9]|9[0-35-9])\d{8}$', '手机号格式错误')]
    # )
    
    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']
        # # 全部关联
        # fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs = {'class':"form-control", 
                                    'placeholder':'请输入' + field.label}
    # @ 验证方法2：定义字段函数
    def clean_mobile(self):
        text_mobile = self.cleaned_data['mobile']
        
        if len(text_mobile) != 11:
            raise ValidationError('手机号长度错误')
        
        if models.PrettyNum.objects.filter(mobile=text_mobile).exists():
           raise ValidationError('手机号已存在') 
        return text_mobile
    


class PrettynumModelForm_edit(forms.ModelForm):
    # # 可以设置手机号不可改
    # mobile = forms.CharField(disabled=True, label='手机号') 
    
    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs = {'class':"form-control", 
                                    'placeholder':'请输入' + field.label}
    
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
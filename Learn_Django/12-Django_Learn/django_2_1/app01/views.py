from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01.utils.pagination import Pagination
from django import forms

# ！ 部门管理
# 部门列表展示
def depart_list(request):
    # 从数据库获取部门信息，queryset类型
    department_list = models.Department.objects.all()
    
    return render(request, 'depart_list.html', 
                  {'department_list' : department_list})

# 添加部门
def depart_add(request):
    if request.method == "GET":
        return render(request, 'depart_add.html')
    
    depart_name = request.POST.get('depart_name')
    
    models.Department.objects.create(title=depart_name)
    
    return redirect('/depart/list')

# 删除部门
def depart_delete(request):
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect("/depart/list")

# 修改部门
def depart_edit(request, nid):
    # 页面点击编辑按钮，提交的是GET请求
    if request.method == 'GET':
        depart_row_data = models.Department.objects.filter(id=nid).first()

        return render(request, 'depart_edit.html', 
                    {"depart_row_data":depart_row_data})
    
    new_depart_name = request.POST.get("new_depart_name")
    models.Department.objects.filter(id=nid).update(title=new_depart_name)
    
    return redirect("/depart/list/")


# ！ 员工管理
# 员工列表
def user_list(request):
    choices_list = {}
    search_result = request.GET.get('search_data', '')
    if search_result:
        choices_list['age__contains'] = search_result
        # choices_list['password__contains'] = search_result
    
    # filter搜索条件如果为空，则等价于.all()
    
    user_list = models.UserInfo.objects.filter(**choices_list)
    return render(request, 'user_list.html',
                  {'user_list':user_list,
                   'search_result':search_result})
       
# 添加员工
def user_add(request):
    if request.method == 'GET':
        context = {
            'gender_choices':models.UserInfo.gender_choices,
            'depart_list':models.Department.objects.all()
        }
        return render(request, 'user_add.html', context)
    
    user_name = request.POST.get("user_name")
    user_password = request.POST.get("user_password")
    user_age = request.POST.get("user_age")
    user_account = request.POST.get("user_account")
    user_ctime = request.POST.get("user_ctime")
    user_gender = request.POST.get("user_gender")
    user_depart = request.POST.get("user_depart")
    
    models.UserInfo.objects.create(name=user_name,
                                   password=user_password,
                                   age = user_age,
                                   account=user_account,
                                   create_time=user_ctime,
                                   gender=user_gender,
                                   Department_id=user_depart)
    return redirect('/user/list/')

# 添加员工-From组件版本
class MyForm(forms.Form):
    name = forms.CharField(label='名字')
    password = forms.CharField(label='密码')
    age = forms.IntegerField(label='年龄')
    account = forms.DecimalField(label='账户余额')
    create_time = forms.DateField(label='创建时间')
    Department = forms.CharField(label='所属部门')
    gender = forms.CharField(label='性别')
      
def user_add_Form(request):
        if request.method == 'GET':
            form = MyForm()
        return render(request, 'user_add_Form.html',
                      {'form':form})
    

# 添加员工-ModelForm组件版本
from django import forms
class UserModelForm(forms.ModelForm):
    
    # 更多校验规则
    name = forms.CharField(min_length=2, label='用户名')
    
    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'account', 'create_time', 'gender', 'Department']
        
        # ！ 实现起来还是麻烦
        # widgets = {
        #     'name':forms.TextInput( attrs={'class':"form-control"} ),
        # }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            if name == 'create_time':
                field.widget.attrs = {'class':"form-control", 
                                  'placeholder': '请输入' + field.label + '【例：2022-01-21】'}
            else:
                field.widget.attrs = {'class':"form-control", 
                                      'placeholder':'请输入' + field.label}

def user_add_ModelForm(request):
    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'user_add_ModelForm.html', 
                      {"form":form})
    
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # 获取数据：form.cleaned_data
        # 保存数据：create操作
        
        # 便捷操作
        form.save()  # 保存到自定义的models.UserInfo类里面
        
        print(form.errors)
        
        return redirect('/user/list/')
    
    return render(request, 'user_add_ModelForm.html', 
                      {"form":form})
    
# 员工编辑
def user_edit(request, nid):
    if request.method == 'GET':
        
        user_row_data = models.UserInfo.objects.filter(id=nid).first()
        
        form = UserModelForm(instance=user_row_data)
        return render(request, 'user_edit.html', 
                    {"form":form})
    
    user_row_data = models.UserInfo.objects.filter(id=nid).first()
    form = UserModelForm(data=request.POST, instance=user_row_data)
    if form.is_valid():
        # 如果有其他的数据也想保存到数据库：form.instance.字段名 = 值
        form.save()
        return redirect('/user/list/')
    
    return render(request, 'user_edit.html', 
                {"form":form})

# 删除员工
def user_delete(request):
    nid = request.GET.get('nid')
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")


# ！ 靓号管理
# 靓号列表
class PrettynumListModelForm(forms.ModelForm):
    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']
        
def prettynum_list(request):
    # @ 批量创建数据，用于学习分页知识    
    # for i in range(300):
    #     models.PrettyNum.objects.create(mobile='12345678901', price='1234', level=2, status=2)
    
    choices_list = {}
    search_key = request.GET.get('search_key')
    print(search_key)

    form = PrettynumListModelForm()
    for field in form:
        print(field, field.name, field.label)
        
    
    search_criteria = request.GET.get('search_criteria', '')  # 有数值拿数值，没数值拿空字符串
    if search_criteria:
        choices_list['mobile__contains'] = search_criteria
        
    data_list_selected = models.PrettyNum.objects.filter(**choices_list).order_by('-level')
    
    pagination_object = Pagination(request, data_list_selected)
    
    form = PrettynumListModelForm()
    context = {
        'prettynum_list':pagination_object.data_list_PerPageShow,
        'search_criteria':search_criteria,
        'page_string':pagination_object.Html_Pagination(),
        'form':form
    }
    return render(request, 'prettynum_list.html', context)
    
# 靓号添加
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
class PrettynumAddModelForm(forms.ModelForm):
    
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
def prettynum_add_ModelForm(request):
    if request.method == "GET":
        form = PrettynumAddModelForm()
        return render(request, 'prettynum_add_ModelForm.html', 
                      {"form":form})
    
    form = PrettynumAddModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/prettynum/list/')
    
    return render(request, 'user_add_ModelForm.html', 
                      {"form":form})
    
   
# 靓号编辑
class PrettynumEditModelForm(forms.ModelForm):
    
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
def prettynum_edit(request, nid):
    if request.method == 'GET':
        
        prettynum_row_data = models.PrettyNum.objects.filter(id=nid).first()
        
        form = PrettynumEditModelForm(instance=prettynum_row_data)
        return render(request, 'prettynum_edit.html', 
                    {"form":form})
    
    prettynum_row_data = models.PrettyNum.objects.filter(id=nid).first()
    form = PrettynumEditModelForm(data=request.POST, instance=prettynum_row_data)
    if form.is_valid():
        form.save()
        return redirect('/prettynum/list/')
    
    return render(request, 'prettynum_edit.html', 
                {"form":form})

# 靓号删除
def prettynum_delete(request):
    nid = request.GET.get('nid')
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect("/prettynum/list/" )

    
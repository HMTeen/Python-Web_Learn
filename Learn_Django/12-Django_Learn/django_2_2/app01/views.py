from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.My_ModelForm import *


"""部门管理"""
def depart_list(request):
    department_list = models.Department.objects.all()
    return render(request, 'depart_list.html', 
                  {'department_list' : department_list})


def depart_add(request):
    if request.method == "GET":
        return render(request, 'depart_add.html')
    
    
    depart_name = request.POST.get('depart_name')
    models.Department.objects.create(title=depart_name)
    return redirect('/depart/list')


def depart_delete(request):
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect("/depart/list")


def depart_edit(request, nid):
    if request.method == 'GET':
        depart_row_data = models.Department.objects.filter(id=nid).first()
        return render(request, 'depart_edit.html', 
                    {"depart_row_data":depart_row_data})
    
    new_depart_name = request.POST.get("new_depart_name")
    models.Department.objects.filter(id=nid).update(title=new_depart_name)
    return redirect("/depart/list/")



"""员工管理"""
def user_list(request):
    # for i in range(50):
    #     # 若使用外键（关联有表格），就要这样提交，例：Derpartment
    #     Department = models.Department.objects.get(id=i%2+4)
    #     models.UserInfo.objects.create(name='gs'+str(i), 
    #                                    password='jkl'+str(i), 
    #                                    age=i+5, 
    #                                    account=i+800,
    #                                    create_time='2022-11-12',
    #                                    gender=i%2+1,
    #                                    Department=Department)
    
    choices_list = {}
    search_result = request.GET.get('search_data', '')
    if search_result:
        choices_list['name__contains'] = search_result
    
    user_list_selected = models.UserInfo.objects.filter(**choices_list)  # filter搜索条件如果为空，则等价于.all()
    
    pagination_object = Pagination(request, user_list_selected)
    context = {
        'user_list':pagination_object.data_list_PerPageShow,
        'search_result':search_result,
        'page_string':pagination_object.Html_Pagination()
    }
    return render(request, 'user_list.html', context)
       

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


def user_add_Form(request):
        if request.method == 'GET':
            form = UserForm_add()
        return render(request, 'user_add_Form.html',
                      {'form':form})
    

def user_add_ModelForm(request):
    if request.method == "GET":
        form = UserModelForm_add()
        return render(request, 'user_add_ModelForm.html', 
                      {"form":form})
    
    form = UserModelForm_add(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    
    return render(request, 'user_add_ModelForm.html', 
                      {"form":form})
    

def user_edit(request, nid):
    if request.method == 'GET':
        user_row_data = models.UserInfo.objects.filter(id=nid).first()
        form = UserModelForm_add(instance=user_row_data)
        return render(request, 'user_edit.html', 
                    {"form":form})
    
    user_row_data = models.UserInfo.objects.filter(id=nid).first()
    form = UserModelForm_add(data=request.POST, instance=user_row_data)
    if form.is_valid():
        form.save()     # 如果有其他的数据也想保存到数据库：form.instance.字段名 = 值
        return redirect('/user/list/')
    
    return render(request, 'user_edit.html', 
                {"form":form})


def user_delete(request):
    nid = request.GET.get('nid')
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")


"""靓号管理"""
def prettynum_list(request):
    # @ 批量创建数据，用于学习分页知识    
    # for i in range(300):
    #     models.PrettyNum.objects.create(mobile='12345678901', price='1234', level=2, status=2)
    
    choices_list = {}
    search_result = request.GET.get('search_data', '')  # 有数值取数值，没数值得到空字符串
    if search_result:
        choices_list['mobile__contains'] = search_result
        
    data_list_selected = models.PrettyNum.objects.filter(**choices_list).order_by('-level')    
    pagination_object = Pagination(request, data_list_selected)
    context = {
        'prettynum_list':pagination_object.data_list_PerPageShow,
        'search_result':search_result,
        'page_string':pagination_object.Html_Pagination()
    }
    return render(request, 'prettynum_list.html', context)
    

def prettynum_add_ModelForm(request):
    if request.method == "GET":
        form = PrettynumModelForm_add()
        return render(request, 'prettynum_add_ModelForm.html', 
                      {"form":form})
    
    form = PrettynumModelForm_add(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/prettynum/list/')
    
    return render(request, 'user_add_ModelForm.html', 
                      {"form":form})
    
   
def prettynum_edit(request, nid):
    if request.method == 'GET':
        
        prettynum_row_data = models.PrettyNum.objects.filter(id=nid).first()
        
        form = PrettynumModelForm_add(instance=prettynum_row_data)
        return render(request, 'prettynum_edit.html', 
                    {"form":form})
    
    prettynum_row_data = models.PrettyNum.objects.filter(id=nid).first()
    form = PrettynumModelForm_add(data=request.POST, instance=prettynum_row_data)
    if form.is_valid():
        form.save()
        return redirect('/prettynum/list/')
    
    return render(request, 'prettynum_edit.html', 
                {"form":form})


def prettynum_delete(request):
    nid = request.GET.get('nid')
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect("/prettynum/list/" )

    
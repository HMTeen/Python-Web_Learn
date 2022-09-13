from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.My_ModelForm import *
from app01.utils.My_Form import *


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
    return render(request, 'user/user_list.html', context)
       

def user_add(request):
    if request.method == 'GET':
        context = {
            'gender_choices':models.UserInfo.gender_choices,
            'depart_list':models.Department.objects.all()
        }
        return render(request, 'user/user_add.html', context)
    
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
        return render(request, 'user/user_add_Form.html',
                      {'form':form})
    

def user_add_ModelForm(request):
    if request.method == "GET":
        form = UserModelForm_add()
        return render(request, 'user/user_add_ModelForm.html', 
                      {"form":form})
    
    form = UserModelForm_add(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    
    return render(request, 'user/user_add_ModelForm.html', 
                      {"form":form})
    

def user_edit(request, nid):
    if request.method == 'GET':
        user_row_data = models.UserInfo.objects.filter(id=nid).first()
        form = UserModelForm_add(instance=user_row_data)
        return render(request, 'user/user_edit.html', 
                    {"form":form})
    
    user_row_data = models.UserInfo.objects.filter(id=nid).first()
    form = UserModelForm_add(data=request.POST, instance=user_row_data)
    if form.is_valid():
        form.save()     # 如果有其他的数据也想保存到数据库：form.instance.字段名 = 值
        return redirect('/user/list/')
    
    return render(request, 'user/user_edit.html', 
                {"form":form})


def user_delete(request):
    nid = request.GET.get('nid')
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")

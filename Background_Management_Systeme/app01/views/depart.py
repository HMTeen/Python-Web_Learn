from django.shortcuts import render, HttpResponse, redirect
from app01 import models

from app01.utils.pagination import Pagination
from app01.utils.My_ModelForm import *
from app01.utils.database_data_process import Data_Create

from app01.views.Layout_Function import *

# ！ 常量
STR_Name = '部门信息'

Models_Category = models.Department
ModelForm_Category_list = DepartmentModelForm_list
ModelForm_Category_add = DepartmentModelForm_add
ModelForm_Category_edit = DepartmentModelForm_edit

def list(request):
    # 创建数据
    # Data_Create().Department()

    context = Views_List_HTML().version_1(request, Models_Category, ModelForm_Category_list)
    context['ModelForm_title'] = '新建' + STR_Name
    context['Table_title'] = STR_Name + '列表'
    return render(request, 'depart/list.html', context)


def add(request):
    if request.method == "GET":
        form = ModelForm_Category_add()
        context = {'form':form,
                   'Table_title':'新建' + STR_Name}
        return render(request, 'depart/add.html', context)
    
    form = ModelForm_Category_add(data=request.POST)    
    if form.is_valid():
        form.save()
        return redirect('/depart/list/')
    
    context = {'form':form,
               'Table_title':'新建' + STR_Name}
    return render(request, 'depart/add.html', context)


def edit(request, nid):
    if request.method == 'GET':
        edit_data = Models_Category.objects.filter(id=nid).first()
        form = ModelForm_Category_edit(instance=edit_data)
        context = {'form':form,
                   'Table_title':'修改' + STR_Name}
        return render(request, 'depart/edit.html', context)
        
    edit_data = Models_Category.objects.filter(id=nid).first()
    form = ModelForm_Category_edit(data=request.POST, instance=edit_data)
    if form.is_valid():
        form.save()
        return redirect('/depart/list/')
    
    context = {'form':form,
               'Table_title':'修改' + STR_Name}
    return render(request, 'depart/edit.html', context)


def delete(request):
    nid = request.GET.get('nid')
    Models_Category.objects.filter(id=nid).delete()
    return redirect("/depart/list")
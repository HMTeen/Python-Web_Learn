from django.shortcuts import render, HttpResponse, redirect
from app01 import models

from app01.utils.pagination import Pagination
from app01.utils.My_ModelForm import *
from app01.utils.database_data_process import Data_Create

from app01.views.Layout_Function import *

# ！ 常量
STR_Name = '靓号信息'

Models_Category = models.PrettyNum

ModelForm_Category_list = PrettynumModelForm_list
ModelForm_Category_add = PrettynumModelForm_add
ModelForm_Category_edit = PrettynumModelForm_edit

def list(request):
    # 创建数据
    # Data_Delete().Delete(Models_Category)
    # Data_Create().PrettyNum()

    context = Views_List_HTML().version_1(request, Models_Category, ModelForm_Category_list)
    context['ModelForm_title'] = '新建' + STR_Name
    context['Table_title'] = STR_Name + '列表'
    return render(request, 'prettynum/list.html', context)


def add(request):
    if request.method == "GET":
        form = ModelForm_Category_add()
        context = {'form':form,
                   'Table_title':'新建' + STR_Name}
        return render(request, 'prettynum/add.html', context)
    
    form = ModelForm_Category_add(data=request.POST)    
    if form.is_valid():
        form.save()
        return redirect('/prettynum/list/')
    
    context = {'form':form,
               'Table_title':'新建' + STR_Name}
    return render(request, 'prettynum/add.html', context)


def edit(request, nid):
    if request.method == 'GET':
        edit_data = Models_Category.objects.filter(id=nid).first()
        form = ModelForm_Category_edit(instance=edit_data)
        context = {'form':form,
                   'Table_title':'修改' + STR_Name}
        return render(request, 'prettynum/edit.html', context)
        
    edit_data = Models_Category.objects.filter(id=nid).first()
    form = ModelForm_Category_edit(data=request.POST, instance=edit_data)
    if form.is_valid():
        form.save()
        return redirect('/prettynum/list/')
    
    context = {'form':form,
               'Table_title':'修改' + STR_Name}
    return render(request, 'prettynum/edit.html', context)


def delete(request):
    nid = request.GET.get('nid')
    Models_Category.objects.filter(id=nid).delete()
    return redirect("/prettynum/list")
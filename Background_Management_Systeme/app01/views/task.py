from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.My_ModelForm import *
from app01.utils.database_data_process import Data_Create

from app01.views.Layout_Function import *

import json

# ！ 常量
STR_Name = '任务信息'

Models_Category = models.Task
ModelForm_Category_list = TaskModelForm_list
ModelForm_Category_add = TaskModelForm_add
ModelForm_Category_edit = TaskModelForm_edit

def add(request):
    context = {
        'data_list':ModelForm_Category_add(),
        'ModelForm_title':STR_Name + '列表',
        'Table_title':'新建' + STR_Name}
    return render(request, 'task/add.html', context)


@csrf_exempt
def add_ajax(request):
    # Ajax请求也可以用ModelForm验证
    form = ModelForm_Category_add(data=request.POST)
    if form.is_valid():
        form.save()
        data_list = {'status':True}
        return JsonResponse(data_list)
        
    # 不能返回redirect，即使也受到也不会跳转
    data_list = {'status':False, 'errors': form.errors}
    return JsonResponse(data_list)


def list(request):
    context = Views_List_HTML().version_1(request, Models_Category, ModelForm_Category_list)
    context['Table_title'] = '新建' + STR_Name
    return render(request, 'task/list.html', context)


def edit(request, nid):
    if request.method == 'GET':
        edit_data = Models_Category.objects.filter(id=nid).first()
        form = ModelForm_Category_edit(instance=edit_data)
        context = {'form':form,
                   'Table_title':'修改' + STR_Name}
        return render(request, 'task/edit.html', context)
        
    edit_data = Models_Category.objects.filter(id=nid).first()
    form = ModelForm_Category_edit(data=request.POST, instance=edit_data)
    if form.is_valid():
        form.save()
        return redirect('/task/list/')
    
    context = {'form':form,
               'Table_title':'修改' + STR_Name}
    return render(request, 'task/edit.html', context)


def delete(request):
    nid = request.GET.get('nid')
    Models_Category.objects.filter(id=nid).delete()
    return redirect("/task/list")
    
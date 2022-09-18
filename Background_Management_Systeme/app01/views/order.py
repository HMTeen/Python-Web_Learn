from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from django.views.decorators.csrf import csrf_exempt
from app01.utils.pagination import Pagination
from app01.utils.My_ModelForm import *
from app01.utils.database_data_process import Data_Create
from app01.views.Layout_Function import *
from django.http import JsonResponse
import json
import random
from datetime import datetime

# ！ 常量
STR_Name = '订单信息'

Models_Category = models.Order
ModelForm_Category_list = OrderModelForm_list
ModelForm_Category_add = OrderModelForm_add
ModelForm_Category_edit = OrderModelForm_edit



def list(request):
    # 创建数据
    # Data_Delete().Delete(Models_Category)
    # Data_Create().PrettyNum()

    context = Views_List_HTML().version_1(request, Models_Category, ModelForm_Category_list)
    context['ModelForm_title'] = '新建' + STR_Name
    context['Table_title'] = STR_Name + '列表'
    context['form'] = ModelForm_Category_add()
    return render(request, 'order/list.html', context)


@csrf_exempt
def add(request):
    form = ModelForm_Category_add(data=request.POST)
    if form.is_valid():
        form.instance.oid = datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(1000, 9999))
        form.instance.admin_id = request.session['info']['id']
        
        form.save()
        data_list = {'status':True}
        return JsonResponse(data_list)
        
    data_list = {'status':False, 'errors': form.errors}
    return JsonResponse(data_list)


def edit_normal(request, nid):
    if request.method == 'GET':
        edit_data = Models_Category.objects.filter(id=nid).first()
        form = ModelForm_Category_edit(instance=edit_data)
        context = {'form':form,
                   'Table_title':'修改' + STR_Name}
        return render(request, 'order/edit.html', context)
        
    edit_data = Models_Category.objects.filter(id=nid).first()
    form = ModelForm_Category_edit(data=request.POST, instance=edit_data)
    if form.is_valid():
        form.save()
        return redirect('/order/list/')
    
    context = {'form':form,
               'Table_title':'修改' + STR_Name}
    return render(request, 'order/edit.html', context)


def edit_ajax(request):
    data_list = {'status':True, 'errors': 0, 'page_data':0}
    uid = request.GET.get('uid')
    edit_data = Models_Category.objects.filter(id=uid).first()
    
    if not edit_data:
        data_list['status'] = False
        data_list['errors'] = '数据不存在'
        return JsonResponse(data_list)
    
    # 方法1：对象中取值
    # data_list['page_data'] = {
    #     'name' : edit_data.name,
    #     'price' : edit_data.price,
    #     'status' : edit_data.status,
    # }
    
    # 方法2：直接取到数值
    data_list['page_data'] = Models_Category.objects.filter(id=uid).values('name', 'price', 'status').first()
    
    return JsonResponse(data_list)


@csrf_exempt
def edit_ajax_return(request):
    data_list = {'status':True, 'errors': 0, 'tips':0}
    uid = request.GET.get('uid')
    edit_data = Models_Category.objects.filter(id=uid).first()
    
    if not edit_data:
        data_list['status'] = False
        data_list['tips'] = '数据不存在'
        return JsonResponse(data_list)
    
    
    form = ModelForm_Category_edit(data=request.POST, instance=edit_data)
    if form.is_valid():
        form.save()
        data_list = {'status':True}
        return JsonResponse(data_list)
        
    data_list = {'status':False, 'errors': form.errors}
    return JsonResponse(data_list)


def delete_normal(request):
    nid = request.GET.get('nid')
    Models_Category.objects.filter(id=nid).delete()
    return redirect("/order/list")


def delete_ajax(request):
    data_list = {'status':True, 'errors': 0}
    uid = request.GET.get('uid')
    is_exists =  Models_Category.objects.filter(id=uid).exists()
    if not is_exists:
        data_list['status'] = False
        data_list['errors'] = '数据不存在'
    
    Models_Category.objects.filter(id=uid).delete()
    return JsonResponse(data_list)
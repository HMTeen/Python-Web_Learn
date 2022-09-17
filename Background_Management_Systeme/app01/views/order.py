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

ModelForm_Category_add = OrderModelForm_add
ModelForm_Category_edit = OrderModelForm_edit

def list(request):
    # 创建数据
    # Data_Delete().Delete(Models_Category)
    # Data_Create().PrettyNum()

    context = Views_List_HTML().version_1(request, Models_Category)
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


def edit(request, nid):
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


def delete_normal(request):
    nid = request.GET.get('nid')
    Models_Category.objects.filter(id=nid).delete()
    return redirect("/order/list")
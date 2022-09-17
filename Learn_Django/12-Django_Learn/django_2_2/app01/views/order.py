from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from app01.utils.My_ModelForm import OrderModelForm
from app01 import models

import random
from datetime import datetime


def order_list(request):
    form = OrderModelForm()
    forms = models.Order.objects.all()    
    return render(request, 'order/order_list.html',
                  {'forms':forms,
                   'form':form})


@csrf_exempt
def order_add(request):
    # Ajax请求也可以用ModelForm验证
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        # 用户没有输入订单id信息，得自己添加
        form.instance.oid = datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(1000, 9999))
        
        # 将当前用户的id作为订单信息的id，填写到数据库，而不是用户自己输入
        form.instance.admin_id = request.session['info']['id']
        form.save()
        data_list = {'status':True}
        return JsonResponse(data_list)
        
    # 不能返回redirect，即使也受到也不会跳转
    data_list = {'status':False, 'errors': form.errors}
    return JsonResponse(data_list)
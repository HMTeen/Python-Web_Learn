from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from app01.utils.My_ModelForm import TaskModelForm
from app01 import models

# Ajax应用
def task_list(request):
    
    form = TaskModelForm()
    return render(request, 'task/task_list.html',
                  {'form':form})

@csrf_exempt
def task_add(request):
    # Ajax请求也可以用ModelForm验证
    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_list = {'status':True}
        return JsonResponse(data_list)
        
    # 不能返回redirect，即使也受到也不会跳转
    data_list = {'status':False, 'errors': form.errors}
    return JsonResponse(data_list)
    



# Ajax学习

# 提交信息免除csrf_token验证
@csrf_exempt
def task_ajax(request):
    
    if request.method == 'GET':
        print(request.GET)
        # return HttpResponse('get-成功！')
        
        # # 要将字典用json处理一下，才能以字典形式返回给前端。方便后续调用
        # data_list = {'status':True, 'data':[11, 22, 33]}
        # return HttpResponse(json.dumps(data_list))
        
        # django也有自带的处理函数：JsonResponse，等同于上述操作
        data_list = {'status':True, 'data':[11, 22, 33]}
        return JsonResponse(data_list)
        
    else:
        print(request.POST)
        return HttpResponse('post-成功！')
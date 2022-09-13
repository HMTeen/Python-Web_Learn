from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.My_ModelForm import *


from django.contrib import messages


def admin_list(request):
    
    # # 检查用户是否登录
    # info = request.session.get('info')
    # if not info:
    #     return redirect('/login/')
    
    
    # # 批量创建数据，用于学习分页知识    
    # for i in range(50):
    #     models.Admin.objects.create(name='gsf'+str(i),
    #                                 password='123' + str(i))
    
    choices_list = {}
    search_result = request.GET.get('search_data', '')  # 有数值取数值，没数值得到空字符串
    if search_result:
        choices_list['name__contains'] = search_result
        
    data_list_selected = models.Admin.objects.filter(**choices_list)    
    pagination_object = Pagination(request, data_list_selected)
    context = {
        'admin_list':pagination_object.data_list_PerPageShow,
        'search_result':search_result,
        'page_string':pagination_object.Html_Pagination()
    }
    return render(request, 'admin/admin_list.html', context)
  
  
def admin_add(request):
    title = '新建管理员信息'
    if request.method == "GET":
        form = AdminModelForm_add()
        return render(request, 'layout_AddPage.html', 
                      {"form":form,
                       'title':title})
    
    form = AdminModelForm_add(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    
    return render(request, 'layout_AddPage.html', 
                    {"form":form,
                    'title':title})
    


def admin_edit(request, nid):
    
    row_data_object = models.Admin.objects.filter(id=nid).first()
    if not row_data_object:
        return HttpResponse('数据不存在')
    
    else:
        if request.method == 'GET':
            admin_row_data = models.Admin.objects.filter(id=nid).first()            
            form = AdminModelForm_edit(instance=admin_row_data)
            return render(request, 'layout_EditPage.html', 
                        {"form":form,
                        'title':'编辑管理员信息'})
        
        admin_row_data = models.Admin.objects.filter(id=nid).first()
        form = AdminModelForm_edit(data=request.POST, instance=admin_row_data)
        if form.is_valid():
            form.save()
            # 信息修改成功，则应该重新登录
            return redirect('/login/')
        
        return render(request, 'layout_EditPage.html', 
                    {"form":form,
                    'title':'编辑管理员信息'})
        
        
        
def admin_delete(request):
    nid = request.GET.get('nid')
    models.Admin.objects.filter(id=nid).delete()
    return redirect("/admin/list/" )


def admin_reset(request, nid):    
    
    row_data_object = models.Admin.objects.filter(id=nid).first()
    title = '重置密码 -- {}'.format(row_data_object.name)
    
    if not row_data_object:
        return HttpResponse('数据不存在')
    
    else:
        if request.method == 'GET':
            admin_row_data = models.Admin.objects.filter(id=nid).first()            
            form = AdminModelForm_reset(instance=admin_row_data)
            return render(request, 'layout_EditPage.html', 
                        {"form":form,
                        'title':title})
        
        admin_row_data = models.Admin.objects.filter(id=nid).first()
        form = AdminModelForm_reset(data=request.POST, instance=admin_row_data)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        
        return render(request, 'layout_EditPage.html', 
                    {"form":form,
                    'title':title})
    
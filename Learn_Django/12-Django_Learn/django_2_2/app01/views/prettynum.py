from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.My_ModelForm import *


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
    return render(request, 'prettynum/prettynum_list.html', context)
    

def prettynum_add_ModelForm(request):
    if request.method == "GET":
        form = PrettynumModelForm_add()
        return render(request, 'prettynum/prettynum_add_ModelForm.html', 
                      {"form":form})
    
    form = PrettynumModelForm_add(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/prettynum/list/')
    
    return render(request, 'prettynum/prettynum_add_ModelForm.html', 
                      {"form":form})
    
   
def prettynum_edit(request, nid):
    if request.method == 'GET':
        
        prettynum_row_data = models.PrettyNum.objects.filter(id=nid).first()
        
        form = PrettynumModelForm_add(instance=prettynum_row_data)
        return render(request, 'prettynum/prettynum_edit.html', 
                    {"form":form})
    
    prettynum_row_data = models.PrettyNum.objects.filter(id=nid).first()
    form = PrettynumModelForm_add(data=request.POST, instance=prettynum_row_data)
    if form.is_valid():
        form.save()
        return redirect('/prettynum/list/')
    
    return render(request, 'prettynum/prettynum_edit.html', 
                {"form":form})


def prettynum_delete(request):
    nid = request.GET.get('nid')
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect("/prettynum/list/" )

    
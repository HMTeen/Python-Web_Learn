from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.My_ModelForm import *


"""部门管理"""
def depart_list(request):
    department_list = models.Department.objects.all()
    return render(request, 'depart/depart_list.html', 
                  {'department_list' : department_list})


def depart_add(request):
    if request.method == "GET":
        return render(request, 'depart/depart_add.html')
    
    
    depart_name = request.POST.get('depart_name')
    models.Department.objects.create(title=depart_name)
    return redirect('/depart/list')


def depart_delete(request):
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect("/depart/list")


def depart_edit(request, nid):
    if request.method == 'GET':
        depart_row_data = models.Department.objects.filter(id=nid).first()
        return render(request, 'depart/depart_edit.html', 
                    {"depart_row_data":depart_row_data})
    
    new_depart_name = request.POST.get("new_depart_name")
    models.Department.objects.filter(id=nid).update(title=new_depart_name)
    return redirect("/depart/list/")
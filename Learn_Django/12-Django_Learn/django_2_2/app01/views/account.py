from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.My_ModelForm import *
from app01.utils.My_Form import *

from app01.utils.Encrypts import *

def login(request):
    
    if request.method == 'GET':
        forms = LoginForm()
        return render(request, 'account/login.html',
                      {'forms':forms})
        
    forms = LoginForm(data=request.POST)
    if forms.is_valid():
        
        admin_object = models.Admin.objects.filter(**forms.cleaned_data).first()
        # 若验证失败
        if not admin_object:
            forms.add_error('password', '用户名或密码错误')
            return render(request, 'account/login.html',
                      {'forms':forms})
        
        # 若验证成功
        request.session['info'] = {'id': admin_object.id, 'name':admin_object.name}
        
        return redirect('/admin/list/')
    
    return render(request, 'account/login.html',
                      {'forms':forms})
    
    
def logout(request):
    request.session.clear()
    return redirect('/login/')
    
from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.My_ModelForm import *
from app01.utils.My_Form import *

from app01.utils.Encrypts import *
from app01.utils.Create_Verification_Picture import check_code

def login(request):
    
    if request.method == 'GET':
        forms = LoginForm()
        return render(request, 'account/login.html',
                      {'forms':forms})
        
    forms = LoginForm(data=request.POST)
    if forms.is_valid():
        
        # code验证码不能参与数据库校验，要把他弹出来
        user_input_code = forms.cleaned_data.pop('code')
                    
        admin_object = models.Admin.objects.filter(**forms.cleaned_data).first()
        # 若验证失败
        if not admin_object:
            forms.add_error('password', '用户名或密码错误')
            return render(request, 'account/login.html',
                      {'forms':forms})
            
        code =  request.session.get('image_code', '')
        if code.upper() != user_input_code.upper():
            forms.add_error('code', '验证码错误')
            return render(request, 'account/login.html',
                      {'forms':forms})
        
        # 若验证成功
        request.session['info'] = {'id': admin_object.id, 'name':admin_object.name}
        request.session.set_expiry(60*60*24*7)  # 用户免登录保存7天限度
        
        return redirect('/admin/list/')
    
    return render(request, 'account/login.html',
                      {'forms':forms})
    
    
def logout(request):
    request.session.clear()
    return redirect('/login/')


def image_code(request):
    img, code_str =  check_code()
    
    request.session['image_code'] = code_str
    request.session.set_expiry(60)

    from io import BytesIO
    stream = BytesIO()
    
    img.save(stream, 'png')
    stream.getvalue()
    
    return HttpResponse(stream.getvalue())
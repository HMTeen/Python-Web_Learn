from django.shortcuts import render, HttpResponse, redirect
import requests

# Create your views here.

# request：默认参数
def index(request):
    return HttpResponse('欢迎使用')

# 默认app目录下，寻找templates文件夹下对应的html文件
# 根据app注册顺序，去所有templates目录里面找
def user_list(request):
    return render(request, 'user_list.html')


def test(request):
    # 字符串传入
    name = '韩朝'  
    # 列表传入
    roles = ['管理员', '老板', '保安']  
    # 字典传入
    user_info = {'name': 'gsf', 'salary':'10000', 'role':'ceo'}  
    # 列表套字典
    data_list = [
        {'name': 'gsf', 'salary':'10000', 'role':'ceo'},
        {'name': 'gs', 'salary':'100', 'role':'ce'},
        {'name': 'g', 'salary':'1', 'role':'c'}
    ]
    # 默认传参传的就是字典类型
    return render(request, 'test.html', 
                  {'n1':name,
                   'n2':roles,
                   'n3':user_info,
                   'n4':data_list
                   })
    

def news(request):
    # ! 测试失败，jsondecodererror
    
    # res = requests.get('http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2021/11/news')
    # data_list = res.json()
    # print(data_list)
    return render(request, "news.html")


def get_response(request):
    # 参数request是一个对象，封装了用户发送过来的所有请求有关数据
    
    # # 1、获取请求方式
    # print(request.method)

    # # 2.1、得到GET请求的数据
    # print(request.GET)    
    # # 2.2、得到POST请求的数据
    # print(request.POST)
    
    # # 3.1、把内容字符串返回给请求者
    # return HttpResponse('strs')
    
    # # 3.2、把HTML返回给用户浏览器
    # return render(request, 'get_response.html')
    
    # # 3.3、让用户浏览器重定向到指定网址：用户自己在向指定地址发请求
    # return redirect('https://www.baidu.com/')
    print(request.method)
    
    # 不能是小写的"get"
    if request.method == 'GET':
        return render(request, 'get_response.html')
    else:
        # print(request.items())
        
        return HttpResponse('登录成功')
    
   
from app01.models import UserInfo
def orm(request):
    # ! 新建【访问几次网址，就添加几次数据】
    # UserInfo.objects.create(name='gsf', 
    #                         password='pwd', 
    #                         age=20)

    # UserInfo.objects.create(name='gs', 
    #                         password='pw', 
    #                         age=10)
    
    # ! 删除数据
    # UserInfo.objects.filter(id=1).delete()  # 筛选删除
    # UserInfo.objects.all().delete()         # 全部删除
    
    # ! 获取数据
    # # 获取所有数据【QuerySet类型，可遍历循环的对象】
    # data_list = UserInfo.objects.all()
    # print(data_list)
    # for obj in data_list:
    #     print(obj.name, obj.password, obj.age)
    
    # # 获取满足筛选条件的数据，仍是QuerySet类型
    # data_list_select = UserInfo.objects.filter(id=1)    # 要获取数据，仍要遍历
    
    # # 获取满足筛选条件的数据，直接是数据对象
    # data_list_select = UserInfo.objects.filter(id=1).first()
    # print(data_list_select.name, data_list_select.password, data_list_select.age)
    
    # ! 改数据
    # UserInfo.objects.filter(name='gs').update(age=999)
    
    return HttpResponse('成功')


def info_list(request):
    # 获取所有用户信息
    data_list = UserInfo.objects.all()
    # print(data_list)
    
    return render(request, 'info_list.html', 
                  {'data_list':data_list})
    
def info_add(request):
    if request.method == 'GET':
        return render(request, "info_add.html")
    
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    # 获取的都是字符串类型数据，要跟数据库中对应位置的数据类型一致
    age = int( request.POST.get('age') )      
    
    UserInfo.objects.create(name = user, 
                            password = pwd, 
                            age = age)
    
    # 跳转到别人家网站，要加全部地址，自我跳转，不用写这些
    return redirect('/info/list/')

def info_delete(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/info/list/")
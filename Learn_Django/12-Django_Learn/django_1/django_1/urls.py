"""django_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app01 import views

urlpatterns = [
    # 默认的对应关系，不用
    # path('admin/', admin.site.urls),
    
    # www.xxx.com/index/  ->  函数
    path('index/', views.index),
    path('user/list/', views.user_list),
    # 模板语法测试
    path('user/test/', views.test),
    
    # 案例：联通新闻中心
    path('user/news/', views.news),
    
    # 请求和响应
    path('getres/', views.get_response),
    
    # orm操作数据库
    path('orm/', views.orm),
    
    
    # ! 案例：用户管理
    # 展示用户列表
    path('info/list/', views.info_list),
    
    # 添加用户
    path('info/add/', views.info_add),
    
    # 删除用户
    path('info/delete/', views.info_delete),
    
]

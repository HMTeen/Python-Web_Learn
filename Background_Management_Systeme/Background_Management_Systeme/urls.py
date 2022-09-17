"""Background_Management_Systeme URL Configuration

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
from app01.views import user_login, depart, user, prettynum, admin, task, order

urlpatterns = [
    # path('admin/', admin.site.urls),
    
    # ！ 用户登录
    # 登陆前页面展示，暂时不需要
    # path('before/login/', user_login.before_login),
    
    path('login/', user_login.login),
    path('image/code/', user_login.image_code),
    path('logout/', user_login.logout),
    
    
    # ！ 部门管理
    path('depart/list/', depart.list),
    path('depart/add/', depart.add),
    path('depart/<int:nid>/edit/', depart.edit),
    path('depart/delete/', depart.delete),
    
    
    # ！ 员工信息管理
    path('user/list/', user.list),
    path('user/add/', user.add),
    path('user/<int:nid>/edit/', user.edit),
    path('user/delete/', user.delete),
    
    
    # ！ 靓号信息管理
    path('prettynum/list/', prettynum.list),
    path('prettynum/add/', prettynum.add),
    path('prettynum/<int:nid>/edit/', prettynum.edit),
    path('prettynum/delete/', prettynum.delete),
    
    # ！ 管理员信息管理
    path('admin/list/', admin.list),
    path('admin/add/', admin.add),
    path('admin/<int:nid>/edit/', admin.edit),
    path('admin/delete/', admin.delete),
    
    # ！ 任务管理
    path('task/add/', task.add),
    path('task/list/', task.list),
    path('task/add_ajax/', task.add_ajax),
    path('task/<int:nid>/edit/', task.edit),
    path('task/delete/', task.delete),
    
    # ！ 订单管理
    path('order/list/', order.list),
    path('order/add/', order.add),
    path('order/<int:nid>/edit/', order.edit),
    path('order/delete/', order.delete_normal),
    
    
]

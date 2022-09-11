"""django_2 URL Configuration
 
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
    # path('admin/', admin.site.urls),
    
    # ！ 部门管理
    # 部门列表展示
    path('depart/list/', views.depart_list),
    
    # 添加部门
    path('depart/add/', views.depart_add),
    
    # 删除部门
    path('depart/delete/', views.depart_delete),
    
    # 编辑部门
    # 带有正则表达的url链接
    path('depart/<int:nid>/edit/', views.depart_edit),
    
    
    # ！ 员工用户管理
    # 员工列表展示
    path('user/list/', views.user_list),
    
    # 添加用户
    path('user/add/', views.user_add),
    path('user/add/Form', views.user_add_Form),
    path('user/add/ModelForm/', views.user_add_ModelForm),
    path('user/<int:nid>/edit/', views.user_edit),
    path('user/delete/', views.user_delete),
    
    
    # ！ 靓号管理
    path('prettynum/list/', views.prettynum_list),
    path('prettynum/add/ModelForm/', views.prettynum_add_ModelForm),
    path('prettynum/<int:nid>/edit/', views.prettynum_edit),
    path('prettynum/delete/', views.prettynum_delete),
    
]

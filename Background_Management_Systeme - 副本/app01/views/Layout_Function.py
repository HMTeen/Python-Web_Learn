from django.shortcuts import render, HttpResponse, redirect
from app01 import models

from app01.utils.pagination import Pagination
from app01.utils.My_ModelForm import *

class Views_List_HTML():
    def __init__(self):
        pass
    
    def version_1(self, request, Models_Category):
        choices_list = {}
        search_result = request.GET.get('search_data', '')
        if search_result:
            choices_list['name__contains'] = search_result
        
        data_list_selected = Models_Category.objects.filter(**choices_list)  # filter搜索条件如果为空，则等价于.all()
        
        pagination_object = Pagination(request, data_list_selected)
        context = {
            'data_list':pagination_object.data_list_PerPageShow,
            'search_result':search_result,
            'page_string':pagination_object.Html_Pagination()
        }
        return context


class Data_Delete():
    def __init__(self):
        pass
    
    def Delete(self, Models_Category):
        Models_Category.objects.all().delete()
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, render, redirect

class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        
        # 排除登陆页面的中间件盘查
        if request.path_info not in ['/login/', '/image/code/']:
            
            info = request.session.get('info')
            if not info:
                return redirect('/login/')
        
    def process_response(self, request, response):
        print('M1.走了')
        return response
    
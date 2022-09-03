from flask import Flask,render_template,request
app = Flask(__name__)

# 仅限GET请求
@app.route('/register', methods=['GET'])
def register():
    return render_template('./register2.html')

# 整合两种类型请求的返回数据
@app.route('/register/info', methods=['get', 'post'])
def register_info():
    if request.method == 'GET':
        print(request.args)
        return 'get注册成功'
    elif request.method == 'POST':
        print(request.form)
        # 单独获取信息
        user_post = request.form.get('user')
        pwd_post = request.form.get('pwd')
        gender_post = request.form.get('gender')
        hobby_list_post = request.form.getlist('hobby')
        city_post = request.form.get('city')
        text_info_post = request.form.get('text_info')
        print(user_post, pwd_post, gender_post, hobby_list_post, city_post, text_info_post)
        return 'post注册成功'

if __name__ == '__main__':
    app.run()



from flask import Flask, render_template, request
app = Flask(__name__)

# 仅限GET请求
@app.route('/register', methods=['GET'])
def register():
    return render_template('./register1.html')

# 提交请求后的返回数据
@app.route('/get/register/info', methods=['get'])
def get_register_info():
    print(request.args)
    print(request.args.get('text_info'))
    return 'get注册成功'

@app.route('/post/register/info', methods=['post'])
def post_register_info():
    print(request.form)
    # 单独获取信息
    user_post = request.form.get('user')
    pwd_post = request.form.get('pwd')
    gender_post = request.form.get('gender')
    hobby_list_post = request.form.getlist('hobby')
    city_post = request.form.get('city')
    more_post = request.form.get('text_info')
    print(user_post, pwd_post, gender_post, hobby_list_post, city_post, more_post)
    return 'post注册成功'


if __name__ == '__main__':
    app.run()



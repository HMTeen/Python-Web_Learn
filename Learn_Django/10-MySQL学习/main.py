from turtle import title
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/index')
def index():

    user = ['test', 'for', 'main', 'big']
    # 1.找到html_file.html文件，读取所有内容
    # 2.找到内容中的“特殊占位符”，将数据替换
    # 3.将替换完成的字符串返回给用户浏览器
    return render_template('./html_file.html', title='中国联通', data_list=user)

if __name__ == '__main__':
    app.run()
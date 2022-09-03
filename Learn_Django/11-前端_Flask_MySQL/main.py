import pymysql
from flask import Flask,render_template,request

# mysql创建链接
conn = pymysql.connect(host='127.0.0.1',
                        port=3306,
                        user='root',
                        passwd='GSF157276',
                        charset='utf8',
                        db='unicom')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

app = Flask(__name__)

@app.route('/add/user', methods=['get', 'post'])
def index():
    if request.method == 'GET':
        return render_template('./add_user.html')

    # print(request.form)
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    mobile = request.form.get('mobile')
    # print(user, pwd, mobile)

    # # 发送指令：方法2
    sql_command = "INSERT INTO admin(username, password, mobile) VALUES(%s, %s, %s); "
    cursor.execute(sql_command, [user, pwd, mobile])
    conn.commit()

    # 关闭
    cursor.close()
    conn.close()

    return '数据添加成功' 


@app.route("/show/user")
def shou_user():
    conn = pymysql.connect(host='127.0.0.1',
                        port=3306,
                        user='root',
                        passwd='GSF157276',
                        charset='utf8',
                        db='unicom')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 获取数据:不需要conn.commit()
    sql_command = "select * from admin"
    cursor.execute(sql_command)
    data_list = cursor.fetchall()
    # 获取所有数据
    print(data_list)

    return render_template('./show_user.html', data_list=data_list)


if __name__ == '__main__':
    app.run()
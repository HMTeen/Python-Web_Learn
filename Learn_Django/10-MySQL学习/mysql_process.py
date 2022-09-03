import pymysql
# 创建链接
conn = pymysql.connect(host='127.0.0.1',
                        port=3306,
                        user='root',
                        passwd='GSF157276',
                        charset='utf8',
                        db='unicom')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# # 发送指令：方法1
# cursor.execute(" INSERT INTO admin(username, password, mobile) VALUES('guo', 'asd', 77345678901); ")
# conn.commit()

# # 发送指令：方法2
# sql_command = "INSERT INTO admin(username, password, mobile) VALUES(%s, %s, %s); "
# cursor.execute(sql_command, ['shuai', 'asd', 77345678901])
# conn.commit()

# # 发送指令：方法3
# sql_command = "INSERT INTO admin(username, password, mobile) VALUES(%(n1)s, %(n2)s, %(n3)s); "
# cursor.execute(sql_command, {'n1':'feng', 'n2':'asd', 'n3':77345678901})
# conn.commit()


# 获取数据:不需要conn.commit()
sql_command = "select * from admin"
cursor.execute(sql_command)
# 获取第一条数据
print(cursor.fetchone())
# 获取所有数据
print(cursor.fetchall())

# 关闭
cursor.close()
conn.close()
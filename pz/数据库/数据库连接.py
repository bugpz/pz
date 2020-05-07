import pymysql

# 连接数据库
# 参数1：mysql服务所在主机ip
# 参数2：用户名
# 参数3：密码
# 参数4：要连接的数据库名

db = pymysql.connect('localhost','root','951103','bugpz')

#
# #创建一个cursor对象
cursor = db.cursor()
#
# sql = "insert into zhmm values (346901284,'bugpz559','bugpz559@qq.com','男',17380624968,'否')"
#
# #执行sql语句
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     #如果提交失败，回滚到上一次数据
#     db.rollback()
# #获取返回的信息
# data = cursor.fetchone()
# print(data)
#
# #断开
# cursor.close()
# db.close()

#查询

sql = "select * from zhmm where isdelete = '否'"

cursor.execute(sql)
number =cursor.fetchall()#条数
data = cursor.fetchone()
r =cursor.rowcount#影响的行数
print(number,end=' ')


cursor.close()
db.close()

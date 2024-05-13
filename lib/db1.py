import pymysql
import sys
sys.path.append('..')


def coon():
    coon=pymysql.connect(
        host="localhost", port=3306,
        user="root", password="root",
        db="p2p", charset="utf8"
    )
    return coon

def query_db(sql):
    # 建立连接
    con=coon()
    # 建立游标
    cur=con.cursor()
    cur.execute(sql)
    result=cur.fetchall()
    return result

def change_db(sql):
    # 建立连接
    con = coon()
    # 建立游标
    cur = con.cursor()
    try:
        # 执行sql
        cur.execute(sql)
        # 提交更改
        con.commit()
    except Exception as e:
        # 回滚
        con.rollback()
    finally:
        # 关闭游标
        cur.close()
        # 关闭连接
        con.close()
# 封装常用数据库操作
# 查询
def check_user(name):
    sql="select * from t_user where user_name ={}".format(name)
    result=query_db(sql)
    return True if result else False

# 添加
def add_user(name,password):
    sql="insert into t_user(user_name,password)value ('{}','{}')".format(name,password)
    change_db(sql)

# 删除
def del_user(name):
    sql="delete from t_user where user_name='{}'".format(name)
    change_db(sql)
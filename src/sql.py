import sqlite3

conn = None
def connect():
    global conn
    if not conn:
        #允许多线程使用
        conn = sqlite3.connect('test.db',check_same_thread = False)
    if conn:
        #没表格自动创建
        create_tb()

def create_tb():
    sql = '''create table if not exists user
       (ID INT PRIMARY KEY     NOT NULL,
       name           TEXT    NOT NULL,
       age            INT     NOT NULL,
       address        CHAR(50),
       salary         REAL);'''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def insert():
    rows = []
    for i in range(10000):
        rows.append(['n{}'.format(i),22,'jerry',20.0])
    cur = conn.cursor()
    sql = """insert into user(
    name,age,address,salary)
    values(?,?,?,?)"""
    cur.executemany(sql,rows)
    conn.commit()

def update(a):
    cur = conn.cursor()
    sql = 'update user set salary=? where name=?'
    cur.execute(sql,[a,'n0'])
    conn.commit()
    print('sqlite3 update ok')

def select(name):
    cur = conn.cursor()
    sql = 'select * from user where name=?'
    cur.execute(sql,[name])
    return cur.fetchone()
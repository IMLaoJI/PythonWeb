import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='northwind',
    charset='utf8',
    # 默认输出元组,cursorclass用于转换为字典表输出
    cursorclass=pymysql.cursors.DictCursor
)

def create_table():
    """创建表"""
    sql = """
        create table book
        (
          ID int AUTO_INCREMENT primary key,
          Title NVARCHAR(200) not null,
          PublishDate DATETIME,
          Price decimal(5,2) default 0.00,
          Discontinued BOOL default 1
        );
    """
    c = conn.cursor()
    result = c.execute(sql)
    c.close()
    conn.commit()
    print(result)

def insert_book():
    """添加数据"""
    # '%s'参数占位
    sql = "insert into book (Title, PublishDate) values (%s, %s)"
    book = ('Python 入门精讲', '2018-1-1')
    books = [
        ('ASP.net 入门精讲', '2018-1-2'),
        ('c# 入门精讲', '2018-1-1'),
        ('PHP 入门精讲', '2018-2-3'),
        ('Django 入门精讲', '2018-3-4'),
        ('Flask 入门精讲', '2018-4-5'),
        ('MySQL 入门精讲', '2018-5-6'),
    ]

    with conn.cursor() as c:
        # result = c.execute(sql, book)
        result = c.executemany(sql, books)
        conn.commit()
    print(result)

def update_price(price=0.00, bid=None):
    """更新数据"""
    sql = "update book set Price = %s where ID = %s"
    with conn.cursor() as c:
        result = c.execute(sql, (price, bid))
        conn.commit()
    print(result)

def remove_book(bid=None):
    """删除数据"""
    sql = "delete from book where ID = %s"
    with conn.cursor() as c:
        c.execute(sql, [bid])
        conn.commit()

def get_top_1():
    """获取价格最高得一本图书"""
    sql = "select * from book order by Price desc limit 1"
    with conn.cursor() as c:
        c.execute(sql)
        row = c.fetchone()
        print(row)

def get_all_books():
    """获取所有图书信息"""
    sql = "select * from book"
    # conn.cursorclass = pymysql.cursors.DictCursor
    with conn.cursor() as c:
        c.execute(sql)
        rows = c.fetchall()
        # rows = c.fetchmany(3)
        for row in rows:
            print(row)

def call_procedure(procname, keyword=''):
    """调用存储过程"""
    with conn.cursor() as c:
        c.callproc(procname, (keyword,))
        rows = c.fetchall()
        for row in rows:
            print(row)

if __name__ == '__main__':
    call_procedure('query_book', 'Django')
    # get_all_books()
    # get_top_1()
    # remove_book(6)
    # update_price(39.00, 3)
    # insert_book()
    # create_table()
    conn.close()


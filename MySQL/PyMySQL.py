import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='northwind',
    charset='utf8'
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

if __name__ == '__main__':
    remove_book(6)
    # update_price(39.00, 3)
    # insert_book()
    # create_table()
    conn.close()


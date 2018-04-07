-- 创建数据库
CREATE DATABASE IF NOT EXISTS contact;
  DEFAULT CHARACTER SET = utf8;

-- 查看数据库
SHOW DATABASES ;

-- 切换数据库
USE contact;

-- 修改数据库
ALTER DATABASE contact
  DEFAULT CHARACTER SET = gbk;

-- 删除数据库
DROP DATABASE contact;

-- ------------------------------------

CREATE DATABASE IF NOT EXISTS sample;
USE sample;

-- 创建表
CREATE TABLE IF NOT EXISTS Book
(
  ID INT AUTO_INCREMENT PRIMARY KEY ,  -- 自增长,主键
  Title NVARCHAR(50) NOT NULL ,
  Author NVARCHAR(20) ,
  Price DECIMAL(5, 2) DEFAULT 0.00 ,  -- DECIMAL,5位,2位小数,默认0.00
  PubDate DATE
);

-- 查看表集合
SHOW TABLES ;

-- 查看表结构
DESC book;

-- 修改表
ALTER TABLE Book
    ADD Stock INT;

-- 删除表
DROP TABLE Book;

-- ------------------------------------
CREATE TABLE dept
(
  ID INT AUTO_INCREMENT ,
  Department NVARCHAR(20) UNIQUE NOT NULL ,
  Tel VARCHAR(20) ,
  CONSTRAINT pk_id
    PRIMARY KEY (ID)
);

-- CHECK语法在MySQL不起效,因保证兼容性仍然保留
 CONSTRAINT chk_gender
   CHECK (Gender IN ('男', '女'))

CREATE TABLE employee
(
  ID INT AUTO_INCREMENT PRIMARY KEY ,
  Name NVARCHAR(20) NOT NULL ,
  Gender NVARCHAR(2) DEFAULT '男' ,
  DeptID INT NOT NULL ,
  Salary DECIMAL(8, 2) DEFAULT 0.00 ,
  Birthdate DATE  ,
  CONSTRAINT fk_deptID
    FOREIGN KEY (DeptID) REFERENCES dept(ID)
);

-- 查询表
SELECT * FROM employee;
SELECT * FROM dept;

-- 向表中插入数据
INSERT INTO dept(Department, Tel) VALUES ('财务部', '010 99998888');
INSERT INTO dept(Department, Tel) VALUES ('市场部', '010 99998888');
INSERT INTO dept(Department, Tel) VALUES ('技术部', '010 99998888');
INSERT INTO dept(Department, Tel) VALUES ('项目应用部', '010 99998888');

INSERT INTO employee (Name, Gender, DeptID, Salary, Birthdate)
    VALUES
      ('Tom', '男', 1, 3900.00, '1990-3-3');
INSERT INTO employee (Name, Gender, DeptID, Salary, Birthdate)
    VALUES
      ('Jerry', '男', 1, 3900.00, '1990-3-3');
INSERT INTO employee (Name, Gender, DeptID, Salary, Birthdate)
    VALUES
      ('Mike', '男', 1, 3900.00, '1990-3-3');
INSERT INTO employee (Name, Gender, DeptID, Salary, Birthdate)
    VALUES
      ('Mary', '女', 3, 3900.00, '1990-3-3');

-- 更新(修改)
UPDATE employee SET DeptID = 2, Salary=9830.00 WHERE ID=2;

-- 删除
DELETE FROM employee WHERE ID=3;

-- 清除表数据(重新添加数据将初始ID编号)
TRUNCATE TABLE employee;

-- ------------------------------------

-- SELECT AS 查看...作为...
SELECT CategoryID, CategoryName AS 分类
FROM category;

-- DISTINCT: 去重
SELECT DISTINCT Department FROM northwind.employee;

-- ORDER BY: 排序(ASC默认升序) ,(DESC降序)
-- LIMIT 3: 限制显示前3条
SELECT * FROM northwind.employee ORDER BY Salary DESC LIMIT 3;
-- LIMIT 3, 3:限制显示前3条之后的3条信息
SELECT * FROM northwind.employee ORDER BY Salary DESC LIMIT 3, 3;


-- WHERE: 条件查询 (<>,!=表示不等于)
-- 比较查询
SELECT * FROM northwind.employee WHERE Department = '生产制造部';
SELECT * FROM northwind.employee WHERE Salary >= 5000.00;
SELECT * FROM northwind.employee WHERE Salary != 5000.00;
SELECT * FROM northwind.employee WHERE BirthDate > '1980-1-1';

-- 模式匹配
SELECT * FROM northwind.employee WHERE Name='许建仁';
SELECT * FROM northwind.employee WHERE Name LIKE '%许%';  -- 查询Name包含'许'的
SELECT * FROM northwind.employee WHERE Name LIKE '%俊';   -- 查询Name以'俊'结尾的
SELECT * FROM northwind.employee WHERE Address LIKE '北京%';   -- 查询Address以'北京'开头的
SELECT * FROM northwind.employee WHERE Address LIKE '___北%';  -- 查询Address第4个字是'北'的

-- 范围查询
SELECT * FROM northwind.employee WHERE Salary >= 2000.00 AND Salary <= 4000.00;
SELECT * FROM northwind.employee WHERE Salary BETWEEN 2000.00 AND 4000.00;
SELECT * FROM northwind.employee WHERE BirthDate BETWEEN '1970-1-1' AND '1980-1-1';
SELECT * FROM northwind.employee WHERE Department = '管理部' OR Department = '生产制造部';
SELECT * FROM northwind.employee WHERE Department IN ('管理部', '生产制造部');
SELECT * FROM northwind.employee WHERE Department NOT IN ('管理部', '生产制造部');

-- 空值NULL查询
SELECT * FROM northwind.employee WHERE Salary IS NULL ;
SELECT * FROM northwind.employee WHERE Salary IS NOT NULL ;

-- ------------------------------------

-- 聚合函数
SELECT * FROM employee;
SELECT COUNT(DISTINCT Department) FROM employee;
SELECT COUNT(*) FROM category;

SELECT SUM(Salary) FROM northwind.employee;
SELECT MAX(Salary) FROM northwind.employee;
SELECT MIN(Salary) FROM northwind.employee;
SELECT AVG(Salary) FROM northwind.employee;

-- 分类汇总
SELECT Department, AVG(Salary) AS 平均薪资, MAX(Salary) AS 最高薪资 FROM northwind.employee GROUP BY Department;
SELECT Department, AVG(Salary) AS 平均薪资, MAX(Salary) AS 最高薪资 FROM northwind.employee GROUP BY Department HAVING 最高薪资 >= 5000.00;

-- ------------------------------------
-- 联合查询 内连接
SELECT product.ProductID, product.ProductName, product.UnitPrice, category.CategoryName -- 查询表
FROM product INNER JOIN category  -- 表明连接
  ON product.CategoryID = category.CategoryID;  -- 表明主外键
-- 别名
SELECT p.ProductID, p.ProductName, p.UnitPrice, c.CategoryName
  FROM product p INNER JOIN category c
  ON p.CategoryID = c.CategoryID;

-- ------------------------------------

-- 创建索引
CREATE INDEX idx_salary
    ON northwind.employee(Salary);

-- 创建视图
CREATE VIEW vw_emp
  AS
    SELECT IDCard, Name, Salary FROM northwind.employee;
-- 查询视图
SELECT * FROM vw_emp;
SELECT Name, Salary FROM vw_emp;

-- ------------------------------------
-- SQL系统全局变量
SELECT @@back_log;  -- 主要连接请求数量
SELECT @@basedir;   -- 安装目录

-- SQL用户定义变量
SET @name='Tom';
SELECT @name;
-- 赋值默认值
SELECT @salary := 0.00;

-- 函数
SELECT abs(-20);      -- 取反
SELECT floor(3.9);    -- 向下取整
SELECT ceil(3.1);     -- 向上取整
SELECT round(3.5);    -- 四舍五入
SELECT sqrt(2);       -- 开平方

SELECT char(65);      -- 查询ASC码中65位置的字符
SELECT upper('abcd'); -- 转换为大写
SELECT concat('abc', 'xyz'); -- 连接字符串

SELECT ADDDATE('2018-1-1', INTERVAL 3 MONTH);  -- 日期加法
SELECT ADDDATE('2018-1-1', INTERVAL 3 DAY);    -- 日期加法
SELECT ADDDATE('2018-1-1', INTERVAL 3 YEAR);   -- 日期加法
SELECT DATEDIFF('2008-8-8', NOW());             -- 日期减法
SELECT NOW();

SELECT CAST(24 AS CHAR);  -- 类型转换

SELECT CONCAT('您的成绩是:' , CAST(24 AS CHAR));
SELECT CONVERT(24,CHAR);

SELECT MD5('123456');  -- 哈希编码

SELECT USER();      -- 当前使用的用户名
SELECT DATABASE();  -- 当前使用的数据库

-- 用户定义函数
delimiter $$
CREATE FUNCTION loop_insert()
  RETURNS INT
  BEGIN
    DECLARE count INT;  -- declare 声明变量
    SET count = 1;       -- set 赋值
    while count <= 100 DO
      insert into contact (Name, Email, Phone, Birthdate, Isvalid)
        values ('User', 'user@xuepy.com', '13988888888', '1992-2-2', 1);
      set count = count + 1;
    end while;
    return count;
  END $$;
delimiter ;

select loop_insert();

-- ------------------------------------
-- 存储过程

-- 定义存储过程
create procedure query_products()
  begin
    select p.ProductID, p.ProductName, p.UnitPrice, c.CategoryName
      from product p
        inner join category c
    on p.CategoryID = c.CategoryID;
  end;

-- 调用存储过程
call query_products();

-- 定义含参存储过程
create procedure query_salary_by_dept(in dept nvarchar(20), out sum_salary decimal(10,2))
  begin
    select sum(Salary) into sum_salary from northwind.employee where Department=dept;
  end;

-- 调用存储过程
call query_salary_by_dept('生产制造部', @sum_salary);
select @sum_salary;


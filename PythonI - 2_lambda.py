def build_html(tag, content, **attrs):
    attr_values = ' '.join([f'{k}="{v}"' for k, v in attrs.items()])
    element = f'<{tag} {attr_values}>{content}</{tag}>'
    return element

print(build_html('a', '优品学派', target="_blank", href="#"))

print('--------------------------------') 

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f'<员工 姓名:{self.name}, 年龄:{self.age}, 工资:{self.salary}>'

    def __repr__(self):
        return f'<员工 姓名:{self.name}, 年龄:{self.age}, 工资:{self.salary}>'

employees = [
    Employee('Tom', 20, 3500),
    Employee('Jerry', 30, 4500),
    Employee('Mike', 40, 2500),
    Employee('Peter', 35, 5500),
    Employee('John', 22, 6500),
    Employee('Max', 32, 7500),
]

# 设定大约三十岁的员工,工资增加 3
# def increment_salary(employees, amount):
#     for emp in employees:
#         if emp.age >= 30:
#             emp.salary = emp.salary + amount

def increment_salary(employees, eligible, amount):
    filter_employees = list(filter(eligible, employees))
    for emp in filter_employees:
        emp.salary = emp.salary + amount
        print(emp)

# def filter_employee(emp):
#     return emp.age >= 30

print(employees)
print('--------------------------------') 
#                           filter_employee
increment_salary(employees, lambda emp: emp.age >= 30, 3)
#                           lambda emp: 'x' in emp.name, 3)
#                           lambda emo: emp.name.startwith('M'), 3)
print('--------------------------------') 

# 一个序列内数字各加 3的方法
L = [1, 2, 33, 22, 46, 32]
# 方法一:
def add_number():
    lst = []
    for x in L:
        lst.append(x+3)
    return lst
x = add_number()
print(x)

# 方法二map:(将序列内的每一个元素都应用指定函数)
def add_number(x):
    return x + 3
y = map(add_number, L)
for i in y:
    print(i)

# 方法三lambda:
z = map(lambda z: z + 3, L)
for p in z:
    print(p)

print('--------------------------------') 

# 找出序列中数值大于 30的
L = [1, 2, 33, 22, 46, 32]
x = filter(lambda i: i > 30, L)
for i in x:
    print(i)

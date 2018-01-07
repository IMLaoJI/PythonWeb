people = ['Tom', 'Jerry', 'Mike', 'John', 'Mary']
scores = [89, 66, 24, 78, 34, 56, 98, 101]

# scores + 3
# 方法一:----------------------------------------
def add_score(l, n):
    result = []
    for x in l:
        result.append(x + n)
    return result
scores_2 = add_score(scores, 3)
print(scores_2)

# 方法二 map:------------------------------------
def add_n(x):
    return x + 3
scores_3 = list(map(add_n, scores))
print(scores_3)

# 方法三 map + lambda:---------------------------
scores_4 = list(map(lambda x: x+3, scores))
print(scores_4)

# 方法四 推导:-----------------------------------
scores_5 = [x+3 for x in scores]
print(scores_5)

# 过滤出大于等于60的分数
def filter_score(n):
    return n >= 60

list(filter(filter_score, scores))      # 方法一
list(filter(lambda x: x>=60, scores))   # 方法二:lambda
[x for x in scores if x >= 60]          # 方法三:推导

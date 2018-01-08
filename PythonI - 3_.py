people = ['Tom', 'Jerry', 'Mike', 'John', 'Mary']
scores = [89, 66, 24, 78, 34, 56, 98, 101]

# 方法一:
def add_score(l, n):
    result = []
    for x in l:
        result.append(x + n)
    return result

scores_2 = add_score(scores, 3)
print(scores_2)

# 方法二 map:
def add_n(x):
    return x + 3
scores_3 = list(map(add_n, scores))
print(scores_3)

#方法三 map lambda:
scores_4 = list(map(lambda x: x+3, scores))
print(scores_4)

#方法四 推导:
scores_5 = [x+3 for x in scores]
print(scores_5)

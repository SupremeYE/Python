#기본적인 표현
print(True)
print(False)
#예시
print(2 > 1)    # 2는 1 초과이다
print(2 < 1)    # 2는 1 미만이다
print(3 >= 2)   # 3은 2 이상이다
print(3 <= 3)   # 3은 3 이하이다
print(2 == 2)   # 2는 2와 같다
print(2 != 2)   # 2는 2와 같지 않다
print("-"*10)
#AND
print("AND")
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#OR
print("OR")
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#NOT
print("NOT")
print(not True)
print(not False)


x = 3
print(x > 4 or (x < 2 or x != 3))

print((4 < 3 and 12 > 10) or 7 == 7)
print(not 4 < 3)
print(not not True)

print(3**2 != 9)

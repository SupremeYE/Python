#1
def f(x):
    return x+1
def g(x):
    return x*x-1
print(f(2)) #print(3)과 같음
print(g(3))
print(f(2)+g(3))


print("="*30)


#2
def f(x):
    print("f시작")
    return x+1 #return을 하게되면 실행중인 함수가 종료된다.
    print("f끝")  #Dead Code

def g(x):
    print("g시작")
    return x*x-1
    print("g끝")
print(f(2)) #print(3)과 같음
print(g(3))
print(f(2)+g(3))


print("="*20)



#return과 print의 차이
def print_square(x):
    print(x*x)
def Get_square(x):
    return x*x

print_square(3)
print(print_square(3))
'''위에 함수print에서 9가출력이 되고 리턴값이 출력이
되어햐 하는데 리턴값이 없으므로 파이썬에서는 None이 출력된다.'''
Get_square(3) #return값이 여기 함수 호출부분은 대체하게된다 즉 9와 같다.
print(Get_square(3))      #print함수를 써야한다.

print("="*20)

def ab(x):
    print(x*x)

print(ab(3))
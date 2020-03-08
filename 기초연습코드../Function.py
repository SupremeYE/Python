#함수

def hello():#헤더
    print("Hello world")
    print("Welcome to CodeIt") #바디

hello()

#파라미터(매개변수개념인듯)
def hello(name):
    print("Hello %s" % (name))
    print("Welcome to CodeIt")

hello("유재석")

#Parameters를 사용하는 경우2
def print_sum(a, b): #매개변수
    print(a+b)
def print_mul(a,b):
    print(a*b)
def print_dev(a,b):
    print("%.2f" %(a/b))
def print_ave(x,y,z):
    print((x+y+z)/3)
print_sum(4, 2)#실행인자
print_mul(3,4)
print_dev(13,3)
print_ave(5,10,15)

#프로그래머스연습

def function(): #블럭이 들어갈 자리
 print('안녕 함수!')
print('첫줄 실행하고')
print() #내장함수
function() #직접 만든 함수
print('끝줄 실행하고')
'''함수는 코드의 덩어리에 이름을 붙인 것이다.
새 함수를 정의할 수 있다.
print는 미리 만들어진 함수이다.
함수를 한번 만들고 나면, 그 안은 잊어버려도 좋다.'''

def print_round(num):
    rounded=round(num)
    print(rounded)
print_round(4.6)
print_round(2.2)
print_round(3.6)


def print_profile(name, age):
    print(name)
    print(age)
my_name="이예은"
my_age=21
print_profile(my_name, my_age)


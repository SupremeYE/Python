#조건문 연습1>
'''people = 3
apple = 20

if people < apple /5:
    print('신나는 사과파티! 배 터지게 먹자')

if apple % people > 0:
    print('사과 수가 맞지 않아! 몇 개는 쪼개 먹자')

if people > apple:
    print('사람이 너무 많아! 몆 명은...')'''

'''#조건문 연습2>
money = True
if money:
    print('택시를 타고 가라')
else:
    print('걸어 가라')

temperature = 15
if temperature <=10:
    print('자켓을 입는다')
else:
    print('자켓을 입지 않는다')'''

#주민등록번호식별기
'''def id_number(a):
    b=len(a)
    if b==14:
        if a.find("-")==6:
            print(a)
        else:
            print("주민등록번호 형식이 잘못됐습니다")
    elif b==13:
        print(a[0:5]+'-'+a[6:13])
    elif b>=15:
        print("주민등록번호는 13자리를 초과할 수 없습니다")
    else:
        print("주민등록번호 형식이 잘못됐습니다")
id_number('111111-2222225')'''

''''#시간조건문
#아래 두 줄의 코드는 변수 hour에 현재 시간을 저장합니다.
#이 코드가 어떻게 동작하는지는 이후 강의에서 다룹니다.
from datetime import datetime
hour = datetime.now().hour

#현재 시간이 12시보다 작을때만 print문을 실행하도록 이 아래줄에 if문을 추가하세요.
if hour<12:
    print('오전입니다.')#if문을 추가한 이후 이 줄은 들여쓰기 되어야 합니다.'''

print('='*10)

'''#3의배수인지 알아보는 코드
number = 15
if number % 3 == 0: #number가 3의 배수인지 확인합니다.
    print("{}는 3의 배수입니다.".format(number))#이 코드는 실행됩니다.

number = 16
if number % 3 == 0: #number가 3의 배수인지 확인합니다.
    print("{}는 3의 배수입니다.".format(number))#이 코드는 실행되지 않습니다.'''


'''#학점계산기    
def print_grade(midterm, final):
    total = midterm + final
    # 코드를 쓰세요.
    if total >=90:
        print('You get an A')
    elif 80<=total<90:
        print('You get a B')
    elif 70<=total<80:
        print('You get a C')
    elif 60<=total<70:
        print('You get a D')
    else:
        print('You fail')

# 테스트
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)'''

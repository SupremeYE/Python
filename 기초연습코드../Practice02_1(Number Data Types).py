#기본 정수형끼리의 사칙연산
print(2+4)
print(10-5)
print(3*3)
print(11%5)
print(2**3)
'''정수형끼리의 계산은 정수값이 나옴'''
#나머지연산
print(20/5)
'''나머지는 예외 정수/정수 해도 소숫값이 나옴'''
print(2+(3+5))
'''괄호안이 먼저 계산'''
print(10-2*2)
'''사칙연산의 규칙에 따라 계산'''
print(10-6/3)
#실수형의 사칙연산
print(2.0+3.0)
print(8.0-5.0)
print(9.0/3.0)
print(2.0*2.0)
print(6.0%4.0)
"""소수끼리의 계산에서는 무조건 소숫값이 나옴"""
print(2.0+3)
print(5.0*2)
print(10-5.0)

#지수표현
e=3.14e3
'''3.14X10의 3승을 의미'''
print(e)
#실수표현
f=2/3
print("%.5f"%f)
'''소수점 이하 자리는 %.f 포멧을 이용하여 출력한다 소수점이하5자리까지 출력'''

#복소수표현
c=2-3j
print(c)
print("실수부:{0}, 허수부:{1}".format(c.real ,c.imag))
print(c.conjugate())
'''켤레 복소수 리턴'''
abs(c)
print(7/4)
print(7//4)

#real, imag 값을 정수/실수로 전달하는 경우
print(complex(1,1))
print(complex(1.1,2.2))
#imag값이 생략되는 경우
print(complex(1))
#두인자가 다 생략되는 경우
print(complex())
#첫번째 인자를 문자열로 전달하는 경우(두번째 인자는 없음)
print(complex("1+1j"))

print(5.0//2)
print(5.0//2.0)
print(5//2.0)

print("round 사용")
print(round(1.421, 1)) #1.421을 소수점 1째 자리로 반올림
print(round(2.7862, 2)) #2.7862를 소수점 2째 자리로 반올림
print(round(4.32)) # 4.32를 소수점 0번째 자리로 반올림




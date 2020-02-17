string='Hello world'
print(len(string))

a="hello world"
print(a[4])
print(string[0])
print(a[-1])
print(a[-2])

a="Hello world"
b=a[0]+a[1]+a[2]+a[3]+a[4]
print(b)

a="Hello world"
print(a[0:5])

a="Hello world"
print(a[0:4])
#0부터 시작하지 않아도 되는표현
a="Life is too short"
print(a[0:4])
print(a[5:11])
print(a[2:8])

print("="*10) #선긋기

#양쪽의 번호를 다 사용하지 않은 경우
print(a[8:])
print(a[:17])
print(a[0:])
print(a[:11])
print(a[:])

#마이너스를 이용한 슬라이싱
print(a[12:-1])
print(a[12:-2])
print(a[12:-3])
print(a[12:-4])

#문자열 중간의 글자 바꾸는 법(슬라이싱 활용)
a="Pithon"
print(a[:1])
print(a[2:])
print(a[:1]+'y'+a[2:])

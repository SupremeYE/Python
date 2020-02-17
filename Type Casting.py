#숫자형->숫자형
print(int(3.8)) #int->정수로변환
print(float(3)) #float->소수로변환

#문자열->숫자형
print(int("2")+int("5")) #print(2+5)
print(float("1.1")+float("2.5")) #print(1.1+2.5)

#숫자형->문자열
#str=>string(문자열)
print(str(2)+str(5)) #print("2"+"5")
print("제나이는 "+str(7)+"살입니다")

#주의!
'''print(int("Hello world")) #논리적으로 변환이 가능한지 생각하기'''

print(float("1.1")+float("4.6"))

print(str(4.0)*2)

year =2016
month =3
day =19
day_of_week="토"
print(str(year)+"년")
print("year"+"년") #str을 써줘야 하는 이유
print("3월")
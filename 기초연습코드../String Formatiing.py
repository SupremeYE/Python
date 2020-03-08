year = 2020
month = 1
date = 12
day_of_week = "일"

print("오늘은 %d년 %d월 %d일 %s요일 입니다"% (year, month, date, day_of_week))
print("오늘은 %d년 %d월 %d일 %s요일 입니다"% (year, month, date+1, "월"))
#소수점 포맷팅
print(1.0/3)
print("1나누기 3은 %d"%(1.0/3)) #정수형만 출력
print("1나누기 3은 %f"%(1.0/3)) #소수점까지 출력
print("1나누기 3은 %.4f"%(1.0/3)) #4자리 까지만 출력
#정수형 포맷팅
print("%d" % 3)
#문자열 포맷팅
print("%s" %"화이팅")
print("%s" % "노력하자")


number=5
print("나는%d개의 사과가 있어"%number)

#코드잇 연습문제
wage = 5                  # 시급 (1시간에 5달러)
exchange_rate = 1142.16   # 환율 (1달러에 1142.16원)

# "1시간에 5달러 벌었습니다." 출력
print("%d시간에 %d%s 벌었습니다." % (1, wage * 1, "달러"))

# "5시간에 25달러 벌었습니다." 출력
print("%d시간에 %d%s 벌었습니다" % (5,wage*5,"달러"))

# "1시간에 5710.8원 벌었습니다." 출력
print("%d시간에 %.1f%s 벌었습니다" % (1,exchange_rate*5,"원" ))
print("%d시간에 %.1f%s 벌었습니다" % (5,wage*1*exchange_rate,"달러"))

# "5시간에 28554.0원 벌었습니다." 출력
print("%d시간에 %.1f%s 벌었습니다" % (5,exchange_rate*25,"원"))
print("%d시간에 %.1f%s 벌었습니다" % (5,wage*5*exchange_rate,"달러"))

print("I have %s apples" % 3)
print("rate is %s" %3.234)


print("%10s" % "hi")
print("%-10sJane" % "hi")

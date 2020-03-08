#연습1
list1 =['가위', '바위', '보']
list2 = [37,23,10,33,29,40]
print(list1, list2)

print(list1[0])
print(list2[3])

#원소바꾸기1
list1[0]='바위'
print(list1[0])
print(list1)


#list에서 음수를 사용하면 뒤에값부터 출력
#print(list1[3])
print(list1[-1])
print(list1[-3])

#연습2
numbers = [1,2,3,4,5,6]
name = ["예은","동준","승연","기찬"]
#인덱싱
print(numbers)
print(name)
print(numbers[0])
print(numbers[0] + numbers[1]) #list의 값을 더할수 있음
print(numbers[-1])

#슬라이싱
print(numbers[0:4])
#원소바꾸기2
numbers[0] = 7
print(numbers)

#원소바꾸기3
numbers = [1, 2, 3, 4, 5, 6]
names = ["윤수", "혜린", "태호", "영훈"]

numbers[0] = 7
print(numbers)

numbers[1] = numbers[1] + numbers[2]
print(numbers)

a=[1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[3])
print(a[-1][0])

a=[1,2,3,['a','b','c'],4,5]
print(a[2:5])
print(a[3][:2])
print(a[3][:3])


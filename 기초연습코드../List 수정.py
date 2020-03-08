list2 = [1,2,3,4,5,6]
print(list2)
#copy()를 사용해 리스트 복사하기
print(list2.copy())

#내림차순sort
'''list2.sort(reverse = True)
print(list2)'''

#요소의 갯수를 확인하는 방법(count)
'''print(list2.count(3))'''

#pop를 사용하여 요소 끄집어내기
'''list2.pop()
print(list2)
list2.pop(2)
print(list2)'''

#원하는 요소 찾기
'''print(1 in list2)
print(7 in list2)'''

#index를 사용해 요소위치반환하기
'''print(list2.index(4))'''


#reverse를 사용해 리스트 뒤집기
'''list2.reverse()
print(list2)'''


#리스트 순서대로 정렬하기
'''list2. sort()
print(list2)'''

#extend를 사용한 리스트추가
'''list2.extend([7,8,9])
print(list2)'''
#insert를 사용한 추가하는 방법
'''list2.insert(0,8)
print(list2)
list2.append(8) #insert와 비교하는 코드
print(list2)'''

#remove를 사용해 리스트요소 제거하기
'''list2.remove(4)
print(list2)'''
#리스트 요소 삭제하기
'''del list2[3]
print(list2)'''
#[]를 사용해 리스트 요소 삭제하기
'''list2[1:3]=[]
print(list2)'''

#연속된 값을 수정할때 주의해야하는 코드
'''list2[1]=['a','b','d']
print(list2)'''


#리스트에서 연속된값 수정하기
'''list2[2:5] = ['a','b','d']
print(list2)'''

#append와 동등한 기능
'''list2[len(list2):]=[7]
print(list2)'''
#리스트에서 하나의 값 수정하기
'''list2[2]=9
print(list2)'''

#리스트값을 추가하는법
'''list2.append(7)
print(list2)

list2.append([8,9])
print(list2)'''

'''list3 = list2+[7]
print(list3)'''

'''list4 = list2+list3
print(list4)'''

#원하는 값이 있는지 확인
'''n=5
if n in list2:
    print('{}은 리스트에 있다'.format(n))'''

#리스트내의 값을 삭제하는법
'''print(list2)
del list2[3]
print(list2)

list2.remove(1)
print(list2)'''

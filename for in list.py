'''patterns = ['가위','바위','보','가위','바위','보']
for pattern in patterns:
    print(pattern)'''
#in 뒤에 있는 모든 값을 in 앞에있는 변수에 한번씩 넣어가면서 실행
#pattern은 for이 만들어낸 변수이다. 리스트의 크기에 상관없이 반복 가능
# for반복문에는 내용을 대입할 반복 변수와 반복하려는 내용이 들어가고 반복할 코드의블럭이 들어간다
#변수의 내용이 순서대로 들어가면서 반복된다.

#for in range사용하기1
'''for i in range(5):
    print(i)'''
#for in range사용하기2
'''names=['예은','동준','승연','기찬']
for i in range(4):
    name=names[i]
    print('{}번 {}'.format(i+1,name))'''
#사용하기 3
names = ['예은', '동준', '승연', '기찬','지혜']
'''for i in range(len(names)):
    name = names[i]
    print('{}번 {}'.format(i + 1, name))'''

#enumerate사용하기
for i,name in enumerate(names):
    print('{}번 {}'.format(i+1,name))
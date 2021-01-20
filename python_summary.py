
class list{
    >>> a = [1, 2, 3]
    >>> a.insert(1, 5)

    #list 함수에 리스트를 입력으로 주면 똑같은 리스트를 복사하여 돌려준다.
    #>>> a = [1, 2, 3]
    #>>> b = list(a)

    #=============================================리스트

    a[-1] a[1]

    #슬라이싱
    a[1:5] #2번째 원소부터 5번째 원소까지

    #리스트 컴프리헨션
    #반복문이랑 조건문이 같이 들어가서 리스트를 만듬
    array = [i for i in range(10) if i%2 == 1]

    a.append(i) #자바에서의 add와 같음

    #2차원 리스트를 초기화할때? n*m크기의 리스트를 한번에 초기화 할때
    array = [[0] * m for _ in range(n)]
    # _는 그냥 숫자 안쓰고 반복만 할 때

    a.sort() #오름차순
    a.sort(reverse=True) #내림차순
    a.reverse() #순서 뒤집어 놓음
    a.insert(3, 122) #위치 인덱스, 삽입할 값
    a.count(32) #리스트 상에서 특정 값을 가지는 데이터의 개수를 셀 때
    a.remove(3) #리스트에서 특정한 값을 갖는 원소를 제거, 값을 가진 원소가 여러개면 하나만 제거함

    a.extend([1,2,3])

    #리스트는 클래스 형태 라고도 말할 수 있어서 메소드를 가질 수 있는데, 
    # sort 와 sorted 차이? 
    # sort는 내부적으로 정렬함. 메서드임.
    # sorted는 정렬한 결과의 복제 객체를 반환함. 내부적으로 리스트 자체는 바뀌진 않음. 내장함수임.

    # remove_all같은게 없어서 하나밖에 못지움.
    # 이런 기능을 이용하기 위해 
    a = [1,2,3,3,4,4,5,5,5]
    remove_set={3,5}
    #remove_list에 포함되지 않은 값만을 저장
    result = [i for i in arr if i not in remove_set]

    # 자바나 C++은 ' 문자 ' " 문자열 " 인데
    #파이선은 큰따옴표 작은따옴표 둘다.
    # \문자 붙여서 안쪽에서 사용 가능

    # 문자열 덧셈
    # "abcdef" 도 슬라이싱 가능
    # 
    # 튜플은 한 번 선언된 값을 변경할 수 없음.
    # 튜플은 소괄호 이용함.
}

class dictionary{
    # 사전 자료형
    # 키 key 값 value 의 쌍을 데이터로 가지는 자료형
    # 데이터 검색 수정에 있어서 O(1)의 시간에 처리 가능.
    data = dict()
    data['key'] = 'Value'

    if 'key' in data: 
        print('존재')

    # 사전에서 키 또는 값만 따로 뽑아낼 수 있음
    #data.keys() 이것만 하면 dict_keys() 자료형임
    #data.values() 이것만 하면 dict_values() 자료형임
    keylist = list(data.keys())
}

class map{
    #!!!!!!!!!
    #map(f, iterable)은 '함수(f)'와 반복 가능한('iterable') 자료형을 입력으로 받는다. 
    #map은 입력받은 자료형의 '각 요소를' '함수 f가 수행한 결과'를 묶어서 돌려주는 함수이다.
    >>> def two_times(x): 
    ...     return x*2
    ...
    >>> list(map(two_times, [1, 2, 3, 4]))
    [2, 4, 6, 8]

}

class set{
    #=============================================집합

    #집합 자료형 : 어떤 정수가 나왔는지 안나왔는지 알아볼때 
    # 순서 없어서 인덱싱 못함. 키값으로 접근함.
    # 리스트를 셋으로 바꾸는법 set(list)
    set_ex = {1,2,3}
    set_ex.add(5)
    print(2 in set_ex) # True
    # 합집합, 교집합, 차집합 존재.

    x = [1,2,3,4,5]
    print(3 in x)
    #복잡도 n임 (리스트길이)

    x = {1,2,3,4,5}
    print(3 in x)
    # 복잡도 상수시간 

    #합집합 a | b
    #교집합 a & b
    #차집합 a - b

    data = set([1,2,3])
    data.add(4)
    data.update([5,6])
    data.remove(3)
}

class for_plus_list_comprehension{
    for idx, i in enumerate(numbers):


    for j in numbers[2:]:
        or
    for j in numbers[idx+1:]:


    #pass 키워드 if문 등에서 그냥 지나갈때. 

    # result ="Success" if score>=80 else "Fail"

    #for i in range(5,100, 3) // start end step :=> 5 8 11 ...
}

class extra_functions{
    round(num, 2) #2째자리 까지 출력
    
    list.sort()는 return nothing


    x or y == if x is false, then y, else x
    x and y == if x is false, then x, else y


    int(x, radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환하여 돌려준다.
    #2진수로 표현된 11의 10진수 값은 다음과 같이 구한다.
    #>>> int('11', 2)
    #3

    #16진수로 표현된 1A의 10진수 값은 다음과 같이 구한다.
    #>>> int('1A', 16)
    #26


    #all(x)는 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며 이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 돌려준다.
    >>> all([1, 2, 3])
    True
    #any(x)는 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며  x의 요소 중 하나라도 참이 있으면 True를 돌려주고
    >>> any([1, 2, 3, 0])
    True

    #chr(i)는 아스키(ASCII) 코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수
    >>> chr(97)
    'a'

    #divmod(a, b)는 2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수이다.
    >>> divmod(7, 3)
    (2, 1)

    #filter
    >>> list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])) #리스트를 복사해서 반환해줌. 그냥 필터만 하면 안나옴.
    [1, 2, 6]




    # 전역변수의 경우
    a =3

    def func():
        global a
        a += 3


    # 함수는 여러개의 반환값을 가질 수 있다.

    print((lambda a,b: a+b)(3,5))


    # result = eval("(3+6)*3")

    from itertools import combinations permutations
    data =['a','b','c']
    result=list(permutations(data, 2))
    result=list(combinations(data, 2))
    result=list(product(data,repeat=2))



    #=============================================표준 입력 방법
    #input()함수는 한 줄을 문자열을 입력받음
    #Map()함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용함.
    #1. map(int, input().split()) 인풋의 각 원소를 int로 매핑함.
    #2. list(map(int, input().split()))

    #ex) 5개 데이터를 받을 때 1,2,3,4,5
    # a,b,c,d,e = map(int, input().split()) => map([1,2,3,4,5]) 원소들이 int가 되도록 매핑
    # print(a,b,c,d,e) => 1 2 3 4 5

    #데이터의 개수 
    n = int(input())
    data = list(map(int, input().split()))

    # import sys
    # sys.stdin.readline().rstrip() #메서드 : 빠르게 입력받을때

    # print() 줄바꿈 포함 안하려면 print(12313, end='')

}
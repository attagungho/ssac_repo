'''
do it 자료구조와 함게 배우는 알고리즘 입문 : 파이썬 편
해시법 중 체인법으로 구현
'''


import hashlib

class Node:
    '''해시를 구성하는 노드'''

    def __init__(self, key, value, next):
        '''초기화'''
        self.key = key
        self.value = value
        self.next = next

class ChainedHash:
    '''체인법으로 해시 클래스 구현'''

    def __init__(self, capacity):
        '''초기화'''
        self.capacity = capacity
        self.table = [None] * self.capacity # 테이블 attribute 이름으로 빈 저장 장소 만들기

    def hash_value(self, key):
        '''해시값 계산'''
        if isinstance(key, int): # key가 int 형이라면  ; isinstance(객체, 자료형) -> bool
            return key % self.capacity # 키를 그대로 저장 공간 길이로 나눠서 그대로 해시 값으로 활용
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity) 
'''
int(hashlib.sha256(str(123).encode()).hexdigest(), 16)

str(123).encode() # binary string으로 만들기
hashlib.sha256(str(123).encode()) # 바이트 문자열의 해시값을 구함 
hashlib.sha256(str(123).encode()).hexdigest() # hash값을 16진수 문자열로 꺼냄
int(hashlib.sha256(str(123).encode()).hexdigest(), 16) #16진수로 표현된 수를 10진수 정수로 바꾸기
hashlib 안불러오고 hash() 도 파이썬 기본 함수에 있다.
'''

'''
라이브러리 없이 기본 해시 함수를 사용하면 입력값에 대한 10진수 정수 해시값을 반환하므로 
입력 시 바이트 문자열 변환, 해시값의 10진수 변환 없이 그대로 사용해도 된다.
    def hash_with_basehash(self, key):
        if isinstance(key, int):
            return key % self.capacity
        return hash(key) % self.capacity
'''


    def search(self, key):
        '''키가 key인 원소를 검색하여 값을 반환'''
        hash = self.hash_value(key) # 위에서 정의한 함수로 key의 해시값 받기
        p = self.table[hash] # hash를 키로 하는 table 위치에 포인터 배치

        while p is not None: # 포인터가 비어있을 때 까지 반복
            if p.key == key: # 포인터가 있는 위치의 키 값이 찾고자 하는 key와 동일한가?
                return p.value # 동일하면 값 반환
            p = p.next # 다르면 해당 노드에 연결된 다음 연결리스트로 포인터 이동
        return None # 마지막 연결리스트 까지 원하는 값을 못 찾으면 None 반환

    def add(self, key, value):
        '''키가 hash_value로 얻은 값이고 값이 value인 원소를 추가'''
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None: # 자리가 비어있지 않을 때
            if p.key == key: # 이미 들어 있는 데이터의 key가 입력하려는 데이터의 key와 동일하면 입력 안함.
                return False
            p = p.next # 비어있는 자리 찾기 위해 포인터 이동
        
        temp = Node(key, value, self.table[hash]) # 비어있는 자리 찾으면 노드 만들기 next로 원래 들어 있던 노드 지정
        self.table[hash] = temp # 원 해시 자리에 temp 노드 넣기 이미 들어 있던 노드는 뒤로 밀림
        return True

    def remove(self, key):
        '''키가 key인 원소 삭제'''
        hash = self.hash_value(key) # 해시값 계산
        p = self.table[hash] # 해시 자리 포인터로 지정
        pp = None # pp 포인터는 None

        while p is not None: # 포인터 자리가 비어있지 않을때까지 탐색 ; 연결리스트 끝까지 탐색
            if p.key == key: # 포인터 자리가 찾는 key인지 맞다면
                if pp is None: # 그리고 pp 가 None 이면 ; 첫 탐색에서 바로 찾았으면
                    self.table[hash] = p.next  # 현재 해시값 첫 자리에 다음 노드(p.next)를 넣음
                else: # pp가 None이 아니면 ; 연결리스트 따라서 탐색을 한 적이 있다면
                    pp.next = p.next # pp로 지정해 줬던 지난번 탐색 노드를 지금 탐색한 노드 다음 노드와 연결 ( 지금 탐색한 노드와의 연결 삭제)
                return True
            pp = p # 방금 탐색한 자리를 pp로 지정
            p = p.next # 다음 노드를 탐색하기 위해 포인터를 이동
        return False  # key 값 못 찾았으면 False 반환
    
    def dump(self):
        '''해시 테이블을 덤프(모두 출력)'''
        for i in range(self.capacity):
            p = self.table[i] 
            print(i, end=' ')
            while p is not None:
                print(f'  -> {p.key} ({p.value})', end='')
                p = p.next  
            print()


if __name__ == '__main__':

    a = ChainedHash(2)
    a.add('jane', 100)
    a.add('john', 100)
    a.add('jane', 100)
    a.add('thomas', 100)
    a.add('theodore', 100)
    a.remove('john')
    a.remove('jack')
    a.dump()
from typing import Any

class FixedStack:
    '''고정 길이 스택 클래스 만들기'''

    class Empty(Exception):
        '''비어 있는 FixedStack에 pop() 또는 peek() 할 때 내보낼 예외 처리'''
        pass

    class Full(Exception):
        '''가득 찬 FixedStack에 push()할 때 내보낼 예외 처리'''
        pass

    def __init__(self, capacity : int= 256) -> None:
        '''FixedStack 초기화'''
        self.stk = [None] * capacity    # 스택 본체
        self.capacity = capacity        # 스택 크기
        self.ptr = 0                    # 스택 포인터

    def __len__(self) -> int:
        '''스택에 쌓여 있는 데이터 개수 반환'''
        return self.ptr                 # 데이터가 들어갈 때 마다 들어간 데이터의 다음 인덱스에 포인터를 위치시켜야 하겠다.

    def is_empty(self) -> bool:
        '''스택이 비어있는지 판단'''
        return self.ptr <= 0            # 포인터 위치로 길이를 판단할 수 있게 만들 것이므로 이를 통해 데이터 들어 있는지 확인

    def is_full(self) -> bool:
        '''스택이 가득 차 있는지 판단'''
        return self.ptr >= self.capacity    # 포인터가 스택 용량보다 큰지 판단

    def push(self, value: Any) -> None:
        '''스택에 value를 입력'''
        if self.is_full():              # 스택이 가득 차 있으면 예외처리
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        '''스택에서 데이터를 꺼냄'''
        if self.is_empty():             # 스택이 비어 있으면 예외처리
            raise FixedStack.Empty
        self.ptr -= 1                   # 데이터를 삭제하지는 않는다. 포인터만 마지막 데이터 위치로 이동시킨다.
        return self.stk[self.ptr]       # 마지막으로 입력된 데이터 반환하고 끝 push가 있으면 덮어 씌워질 것이다. 메모리는 계속 차지할 듯.

    def clear(self) -> None:
        '''모든 데이터를 삭제'''
        self.ptr = 0                    # 포인터를 스택 제일 첫 인덱스로 바꾼다.

    def find(self, value: Any) -> Any:
        '''스택에서 value를 찾아 인덱스를 반환(없으면 -1을 반환)'''
        for i in range(self.ptr -1, -1, -1):    # 포인터 위치한 곳 - 1(top) 부터 인덱스 0까지 역순으로 내려온다. 포인터 뒤로는 검색 안한다.
            if self.stk[i] == value:    # 선형 검색 시행 원소 순서대로 비교한다.
                return i                # 찾으면 해당 인덱스 반환
        return -1                       # 인덱스 0으로 올 때까지 찾는 값과 동일한 원소가 없으면 for문 종료 되고 -1 반환

    def count(self, value: Any) -> bool:
        '''스택에 있는 value의 개수를 반환'''
        c = 0
        for i in range(self.ptr):       # 스택 시작 인덱스(bottom = 0) 부터 포인터 위치 전(top)까지 반복
            if self.stk[i] == value:    # 선형 검색 시행 원소 순서대로 비교.
                c += 1                  # 검색값과 같은 원소 찾으면 count 1 추가
        return c                        # 반복문 종료 후 c 반환

    def __contains__(self, value: Any) -> bool:     # item이 존재 한다면 True, 그렇지 않으면 False를 반환하는 메소드를 정의합니다. 
        '''스택에 value가 있는지 판단'''
        return self.count(value)                    # x in obj을 작성하여 obj.__contains(x)__ 와 같은 결과를 얻을 수 있다.

    def dump(self) -> None:
        '''스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력'''
        if self.is_empty():             # 위에서 정의한 boolean 형태 반환하는 함수
            print('스택이 비어 있습니다.') 
        else:
            print(self.stk[:self.ptr])



if __name__ == '__main__':
    from enum import Enum
    
    Menu = Enum('Menu', ['푸시', '팝', '피크', '검색', '덤프', '종료'])
    
    def select_menu() -> Menu:
        '''메뉴 선택'''
        s = [f'({m.value}){m.name}' for m in Menu] # Enum 객체가 'Menu' 하위에 리스트로 지정된 name과 value 가 있고 value는 1부터 순서대로 값을 가지는 모양이다.
        while True:
            print(*s, sep='   ', end='') # print에서 for-loop으로 list를 순회하며 출력하는 것을 짧게 할 때 print(asterisk* object) 로 표현 가능
            n = int(input(': '))
            if 1 <= n <= len(Menu):
                return Menu(n)
            
    s = FixedStack(64)                  # 최대 길이 64인 스택

    while True:
        print(f'현재 데이터 개수: {len(s)} / {s.capacity}')
        menu = select_menu()

        if menu == Menu.푸시:
            x = int(input('데이터를 입력하세요.: '))  # 정수만 입력하도록 만들었다. 문자열 입력시 오류 발생. 함수는 모든 데이터를 받게 되어있다. int를 없애면 숫자를 넣어도 문자열로 인식하기는 할 듯.
            try:
                s.push(x)
            except FixedStack.Full:
                print('스택이 가득 차 있습니다.')

        elif menu == Menu.팝:
            try:
                x = s.pop()
                print(f'팝한 데이터는 {x}입니다.')
            except FixedStack.Empty:
                print('스택이 비어 있습니다.')

        elif menu == Menu.피크:
            try:
                x = s.peek()
                print(f'피크한 데이터는 {x}입니다.')
            except FixedStack.Empty:
                print('스택이 비어 있습니다.')
        
        elif menu == Menu.검색:
            x = int(input('검색할 값을 입력하세요.: '))
            if x in s:
                print(f'{s.count(x)}개 포함되고, 맨 앞의 위치는 {s.find(x)}입니다.')
            else:
                print('검색값을 찾을 수 없습니다.')
        
        elif menu == Menu.덤프:
            s.dump()

        else:
            break



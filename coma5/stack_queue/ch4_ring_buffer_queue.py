from typing import Any

class FixedQueue:
    '''
    링 버퍼로 큐 구현하기 ; front, rear 포인터로 맨 앞 원소와 맨 끝 원소를 식별하고 원소를 옮길 필요 없이 front, rear 값을 
    업데이트 하면서 데이터 입력과 꺼내기 실행. 맨 앞, 맨 뒤는 물리적 순서가 아닌 논리적 순서.
    '''

    class Empty(Exception):
        '''비어 있는 FixedQueue에서 디큐 또는 피크할 때 내보내는 예외 처리'''
        pass

    class Full(Exception):
        '''가득 차 있는 FixedQueue에서 인큐할 때 내보내는 예외 처리'''
        pass

    def __init__(self, capacity: int) -> None:
        '''초기화'''
        self.no = 0                     # 현재 데이터 개수
        self.front = 0                  # 맨 앞 포인터
        self.rear = 0                   # 맨 끝 포인터
        self.capacity = capacity        # 큐의 크기
        self.que = [None] * capacity    # 큐 생성

    def __len__(self) -> int:
        '''큐에 있는 모든 데이터 개수를 반환,  len() 을 통해 object.__len__()을 호출할 수 있다.'''
        return self.no                  # self.no가 길이 반영할 수 있는 함수를 만들어야 한다.
    
    def is_empty(self) -> bool:
        '''큐가 비어 있는지 판단'''
        return self.no <= 0

    def is_full(self) -> bool:
        '''큐가 가득 차 있는지 판단'''
        return self.no >= self.capacity

    def enque(self, x:Any) -> None:
        '''데이터 x를 인큐'''
        if self.is_full():              # is_full()은 bool 반환
            raise FixedQueue.Full       # 위에서 만들어둔 Full 예외처리 발생
        self.que[self.rear] = x         # rear 포인터 자리에 x 입력
        self.rear += 1                  # rear 포인터 다음으로 이동
        self.no += 1                    # no 관리(길이)
        if self.rear == self.capacity:  # 끝 포인터가 전체 길이랑 같아지면 (인덱스가 길이 넘어가면)
            self.rear = 0               # rear를 0으로 다시 맞춰서 순환 구조 만들기
    
    def deque(self) -> Any:
        '''데이터를 디큐'''
        if self.is_empty():             # is_empty()는 bool 반환
            raise FixedQueue.Empty      # 위에서 만들어둔 Empty 예외처리 발생
        x = self.que[self.front]        # front 포인터 자리의 값을 x로 받아오기
        self.front += 1                 # front 포인터 다음 인덱스로 변경
        self.no -= 1                    # no 관리(길이)
        if self.front == self.capacity:
            self.front = 0              # enque와 동일하게 순환 구조 만들기
        return x                        # 받아온 x 반환

    def peek(self) -> Any:
        '''큐에서 데이터를 피크(맨 앞 데이터 들여다보기)'''
        if self.is_empty():
            raise FixedQueue.Empty      # 비어 있는 경우 예외처리
        return self.que[self.front]     # 맨 앞 데이터를 확인
    
    def find(self, value:Any) -> Any:
        '''큐에서 value를 찾아 인덱스 반환 없으면 -1 반환'''
        for i in range(self.no):                     # 전체 길이 만큼 값이 들어 있으니 전체 길이로 for 반복을 한다.
            idx = (i + self.front) % self.capacity   # front 포인터 부터 값이 시작하니 front를 더하고 rear가 capacity를 넘어가면 순환하니 나머지를 구한다.
            if self.que[idx] == value:               # 검색 성공
                return idx
        return -1                                # 검색 실패

    def count(self, value:Any) -> bool:
        '''큐에 있는 value의 개수를 반환 위와 동일하게 전체 순차 탐색 하면서 검색하면서 count 함'''
        c = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity  
            if self.que[idx] == value:
                c += 1
        return c

    def __contains__(self, value:Any) -> bool:
        '''큐에 value가 있는지 판단'''
        return self.count(value)  # count() 정수를 반환하지만 __contains__는 x in obj 로 bool 판탄 하는 표현으로 접근하므로 0이 아닌 정수값은 자동으로 True bool 값으로 변환되나?

    def clear(self) -> None:
        '''큐의 모든 데이터를 비움'''
        self.no = self.front = self.rear = 0 # 데이터를 지우는 건 아니고 위에서 큐가 비어있는지 판단할 때와 값 접근에 사용했던 길이, 포인터를 모두 초기화

    def dump(self) -> None:
        if self.is_empty():
            print('큐가 비었습니다.')
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end='')
            print()

if __name__ == '__main__':
    ring_queue = FixedQueue(5)
    for i in range(5):
        ring_queue.enque(i)
        print(f'enqued {i}')
    for j in range(5):
        print(f'finding {j}')
        if j in ring_queue:
            print(f'j가 ring_queue에 있나요? : {j in ring_queue}')
            print(f'매직 메소드 직접 접근 : {ring_queue.__contains__(j)}')
            print(f'find 결과 : {ring_queue.find(j)}')
            print(f'count 결과 : {ring_queue.count(j)}')

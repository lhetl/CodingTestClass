from collections import deque
# 빈 deque 생성
my_deque = deque()
# 뒤쪽에 원소 추가
my_deque.append(1)
my_deque.append(2)
my_deque.append(3)
# 앞쪽에 원소 추가
my_deque.appendleft(0)
# 덱 출력: deque([0, 1, 2, 3])
print(my_deque)
# 앞쪽 원소 제거
my_deque.popleft()
# 덱 출력: deque([1, 2, 3])
print(my_deque)
# 뒤쪽 원소 제거
my_deque.pop()
# 덱 출력: deque([1, 2])
print(my_deque)
# 앞쪽에 여러 원소 한 번에 추가
my_deque.extendleft([-2, -1, 0])
# 덱 출력: deque([0, -1, -2, 1, 2])
print(my_deque)
# 뒤쪽에 여러 원소 한 번에 추가
my_deque.extend([3, 4, 5])
# 덱 출력: deque([0, -1, -2, 1, 2, 3, 4, 5])
print(my_deque)
# 덱의 길이 확인
print(len(my_deque)) # 출력: 8
# 덱에서 원소 검색
print(2 in my_deque) # 출력: True
print(6 in my_deque) # 출력: False
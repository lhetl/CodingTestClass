import heapq

q=[]
heapq.heappush(q,(4,10))
heapq.heappush(q,(1,10))
heapq.heappush(q,(3,10))
heapq.heappush(q,(2,10))
v=heapq.heappop(q)
print(v)
v=heapq.heappop(q)
print(v)
v=heapq.heappop(q)
print(v)

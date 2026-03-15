import heapq

patients = [
    ("김철수", 3),
    ("이영희", 1),
    ("박민수", 2)
]

heap = []

for name, priority in patients:
    heapq.heappush(heap, (priority, name))


for j in range(0, len(heap)):
    print(heapq.heappop(heap))
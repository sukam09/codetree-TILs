import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
q = deque(a)
r = deque([0] * n)
cnt = 0
ans = 1

while 1:
    q.rotate(1)
    r.rotate(1)
    if r[-1] == 1:
        r[-1] = 0
    for i in range(len(r) - 2, -1, -1):
        if r[i] == 1 and r[i + 1] == 0 and q[i + 1] >= 1:
            r[i + 1] = 1
            r[i] = 0
            q[i + 1] -= 1
            if q[i + 1] == 0:
                cnt += 1
    if r[-1] == 1:
        r[-1] = 0
    if q[0] > 0:
        r[0] = 1
        q[0] -= 1
        if q[0] == 0:
            cnt += 1
    if cnt >= k:
        break
    ans += 1

print(ans)
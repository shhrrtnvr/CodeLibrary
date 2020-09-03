from collections import deque

if __name__ == '__main__':
    Q = deque()
    Q.append(2)
    Q.append(4)
    print(Q)
    print(Q.popleft())
    Q.extend((3, 6, 1))
    print(Q)
    Q.rotate(2)
    print(Q)
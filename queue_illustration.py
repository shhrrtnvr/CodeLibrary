from queue import Queue

if __name__ == '__main__':
    Q = Queue()
    Q.put(2)
    Q.put(4)
    Q.put(1)
    print(Q.get())
    print(Q.get())
    print(Q.empty())
    print(Q.get())
    print(Q.empty())


import heapq
import itertools


class PriorityQueue:
    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.REMOVED = '<removed-task>'
        self.counter = itertools.count()

    def push(self, task, priority=0):
        if task in self.entry_finder:
            self.remove(task)
        count = next(self.counter)
        entry = [priority, count, task]  # lowest pops first
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)

    def remove(self, task):
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop(self):
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
            return task
        return None


if __name__ == '__main__':
    pq = PriorityQueue()
    pq.push(6, 6)
    pq.push(8, 8)
    pq.push(4, 4)
    print(pq.pop())
    pq.push(14, 14)
    pq.push(3, 3)
    print(pq.pop())
    print(pq.pop())
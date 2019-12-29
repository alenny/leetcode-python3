import threading
from collections import deque

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = deque()
        self.enqueueSema = threading.Semaphore(capacity)
        self.dequeueSema = threading.Semaphore(0)
        self.lock = threading.Lock()

    def enqueue(self, element: int) -> None:
        self.enqueueSema.acquire()
        self.lock.acquire()
        try:
            self.queue.append(element)
            self.dequeueSema.release()
        finally:
            self.lock.release()

    def dequeue(self) -> int:
        self.dequeueSema.acquire()
        self.lock.acquire()
        try:
            val = self.queue.popleft()
            self.enqueueSema.release()
            return val
        finally:
            self.lock.release()

    def size(self) -> int:
        return len(self.queue)
class CreateQueue:
    def __init__(self, size):
        self.size = size
        self.queue = []

    def is_empty(self):
        if not self.queue:
            return True
        else:
            return False

    def is_full(self):
        if len(self.queue) == self.size:
            return True
        else:
            return False
    
    def add_q(self, *item):
        for i in item:
            if self.is_full():
                print("queue is full unable to add")
            else:
                self.queue.append(i)
    
    def delete_q(self):
        if self.is_empty():
            print("queue is empty")
        else:
            queue_front = self.queue[0]
            self.queue.remove(queue_front)
            return queue_front
    
    def print_q(self):
        return self.queue
    


queue = CreateQueue(6)
print(queue.is_empty())
print(queue.is_full())
queue.add_q(2)
queue.add_q(1)
queue.add_q(*(1,2,3,4,5))
print(queue.is_full())
print(queue.print_q())
print(f"{queue.delete_q()} 삭제")
print(queue.print_q())
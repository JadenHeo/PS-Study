class MyStack(object):
    def __init__(self):
        self.lst = list()

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)

class MyQueue(object):
    def __init__(self, max_size):
        self.stack1 = MyStack()
        self.stack2 = MyStack()
        self.max_size = max_size

    def qsize(self):
        return self.stack1.size() + self.stack2.size()

    def push(self, item):
        if self.qsize() < self.max_size:
            self.stack1.push(item)
            return True
        else:
            return False

    def pop(self):
        if self.stack2.size() > 0:
            return self.stack2.pop()
        elif self.stack1.size() == 0:
            raise Exception
        else:
            for _ in range(self.stack1.size()):
                self.stack2.push(self.stack1.pop())
            return self.stack2.pop()
    
n, max_size = map(int, input().strip().split(' '))
queue = MyQueue(max_size)

for _ in range(n):
    command = input().strip().split(' ')
    if command[0] == 'SIZE':
        print(queue.qsize())
    elif command[0] == 'POP':
        try:
            print(queue.pop())
        except Exception:
            print(False)
    elif command[0] == 'PUSH':
        print(queue.push(int(command[1])))
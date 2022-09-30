##stacks with queue module

from queue import LifoQueue
stack = LifoQueue(maxsize=9)##limiting number of items to 9

##adding items to the list
stack.put(5)
stack.put(9)
stack.put(1)
stack.put(7)
###checking whether stack is full
print("is stack ful???",stack.full())
###checking for size of stack
print("size of stack=",stack.qsize())
##retrieving the given items
print(stack.get())
print(stack.get())
print(stack.get())
print(stack.get())
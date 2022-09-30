###implementation of stacks using collections.deque
from collections import deque
items=deque()
##addition of items to the stack
items.append("apple")
items.append("car")
items.append("rack")
print(items)
items.pop()##deleting an item
print(items)
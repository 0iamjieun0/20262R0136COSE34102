from stack import Stack

s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Stack size:", s.size())
print("Top element:", s.peek())
print("Popped element:", s.pop())
print("Stack size after pop:", s.size())
print("Is stack empty?", s.is_empty())


print("Adding another element")
s.push(40)
print("New top element:", s.peek())

print("Adding another element")
s.push(40)
print("New top element:", s.peek())

print("Checking the top element")
print("Top:", s.peek())

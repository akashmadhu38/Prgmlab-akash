size=5
stack = [size]
for i in range (0,size):
    a = input("Enter the value to insert:")
    stack.append(a)
print('Initial stack')
print(stack)
print('\nElements poped from stack:')
for i in range(0,size):
    print(stack.pop())
print('\nStack after elements are poped:')
print(stack)


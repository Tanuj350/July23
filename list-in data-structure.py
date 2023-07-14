mobile=['vivo' , 'apple' , 'samsung' , 'realme' , 'redmi']
print(mobile)
mobile.append('redmi')
mobile.extend('iterable')
mobile.insert(3, 'techno')
print('list:' , mobile)
mobile.remove('apple')
print(mobile)
mobile.pop(0)
print(mobile)
mobile.count('redmi')
print(mobile)
mobile.sort()
print (mobile)
mobile.reverse()
print(mobile)
mobile.copy()
print(mobile)
print(mobile.index("redmi"))

# list as a stack
stack=[1,2,3,4,5,6]
stack.append(7)
print (stack)
stack.pop(4)
print (stack)

# list cpmprehension
square=[]
for x in range(10):
    square.append(x**2)
print(square)  
                        #Data Types-1

#ques 1: Create a list with user defined input

g, h, j = input("Enter three numbers").split(",")

list=[]

list.append(g)
list.append(h)
list.append(j)
print(list)

#ques 2:Add the following llist to the above created

given = ["google","apple","facebook","microsoft","tesla"]

list.append(given)

print(list)

#ques 3:count the number of times an object occurs in a list

print(sum(x.count('google') for x in list))

#ques 4:Create a list with numbers and sort it  in ascending order

list1=[1,5,7,9,4]
list1.sort()
print(list1)

#ques 5:

a=[1,2,3]
b=[4,5,6]
c=[]
c.append(a)
c.append(b)
c.sort()
print(c)

#ques 6:implementation of stack and queue

#stack

stack=[4,5,2,6]
stack.pop()
print(stack)
A=input("Enter the number you want to add")
stack.append(A)
print(stack)

#queue

queue=[4,5,2,6]
queue.pop(0)
print(queue)
B=input("Enter the number you want to add")
queue.append(B)
print(queue)


#queue using deque module

from collections import deque
d = deque('ghi')  #new items added
d.append('j')   #appends at the end
d.appendleft('f') #appends at left
print(d)

d.pop() #pops the element at last(right side)
d.popleft()  #pops leftmost element
print(d)


#ques 7: count even and odd numbers

countEven = 0
countOdd = 0

for x in range(1,10):
    if not x % 2:
        print("Even numbers are:"+str(x))
        countEven+=1
    else:
        print("odd numbers are:" + str(x))
        countOdd += 1
print("number of even numbers"+str(countEven))
print("number of even numbers"+str(countOdd))
















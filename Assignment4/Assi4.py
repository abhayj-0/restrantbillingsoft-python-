#ques1:  Find the length of tuples

tup=(1,2,3)
print("length of tuple"+str(len(tup)))

#ques2: Find the largest nd the smallest elements of a tuples

#for minimum
print("the minimum in tuple"+str(min(tup)))

#for maximum
print("the maximum in tuple"+str(max(tup)))

#ques3: WAP to find a product of all elements of a tuple

r = 1
for count in tup:
    r=r*count

print(r)


#SETS
#two stes are as follows:
a={1,2,3}
b={3,4,5}
#ques1:
# 1:diffrence between two lists:
print("the diffrence"+str(a-b))
# 2:Compare two sets
print("the superset",str(a>=b))
print("the subset",str(a<=b))
print("the superset",str(b>=a))
print("the subset",str(b<=a))
# 3:print the result of intersection of sets
print("intersection of sets"+str(a&b))


#dictionries

# 1:Store name and marks of 3 student by user input

d={}

for i in range(0,3):
    a = input("Enter your name for "+str(i+1)+"value")
    b = int(input("Enter your marks for " + str(i + 1) + "value"))
    d[a]=b
print(d)

# 2:sort the dictionary on basis of marks

a=sorted(d.values())
print(a)
for v in a:
    for i in d.keys():
        if(d[i]==v):
            print("%s %s"%(i,v))


# 3:
strin = "MISSISSIPPI"
M=strin.count('M')
I=strin.count('I')
S=strin.count('S')
P=strin.count('P')

mis = {'M':M,'I':I,'S':S,'P':P}
print(mis)
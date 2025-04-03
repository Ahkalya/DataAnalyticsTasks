# #String Functions
string = "hello everyone, hope all are doing good"
print(string.upper())  
print(string.lower())  
print(string.capitalize())  
print(string.title())  
print(string.swapcase())  
print(len(string))  
print(string.count("o"))  
print(string.find("everyone"))  
print(string.startswith("hello"))  
print(string.endswith("good"))  
print(string.replace("good", "great"))  
print(string.split())  
words = ["Python", "is", "awesome"]
print(" ".join(words))  
print(string.strip())  
print(string.isalpha())  
print(string.isalnum())  
print(string.isnumeric())  
print(string.islower())  
print(string.isupper())  
print(string.isspace())  

# 2.List Functions
l1=['a','b','c']
#append()
l1.append('d')
print(l1)
#copy()
l2 = l1.copy()
print(l2)
#count()
print(l2.count('a'))
#extend
l2.extend('e')
print(l2)
#index
print("Index",l2.index('b'))
#insert
l2.insert(4,'f')
print(l2)
#pop
print(l2.pop(4))
#remove
print(l2.remove('c'))
print(l2)
#reverse
l2.reverse()
print(l2)
#sort
l2.sort()
print(l2)
#clear
l2.clear()
print(l2)

# 3.tuple
tuple = (12,22,33,12,33,44,55)
#len
print(len(tuple))
#count
print(tuple.count(12))
#index
print(tuple.index(22))
#sorted
sorted(tuple)
print(tuple)
#min
print(min(tuple))
#max
print(max(tuple))
#sum
print(sum(tuple))

# 4.Nested if
mark = int(input("Enter Your mark"))
if(mark>=90 and mark<=100):
    print("You got Grade A")
elif(mark>=80 and mark<=90):
    print("you got grade B")
elif(mark>=60 and mark<=70):
    print("you got grade C")
else:
    print("YOU FAILED, BETTER LUCK NEXT TIME")  

# 5.Palindrome
string = input("Enter the word")
rev_string=""
for i in string:
    rev_string = i + rev_string
if(rev_string == string):
    print("It is a palindrome")
else:
    print("It is not a palindrome")

# 6.Prime Number
num = 7
count=0
for i in range(1,num+1):
    if(num%i==0):
        count+=1
if(count==2):
    print("Prime Number")
else:
    print("Not a Prime Number")

# 8.Fibanocci series
num = int(input("Enter the Limit"))
a=1
b=1
print(a)
print(b)
for i in range(1,num+1):
    c=a+b
    print(c)
    a=b
    b=c


# 8. Even or odd
num = int(input("Enter the Number :"))
if(num==0):
    print("Neither even Nor odd")
elif(num%2==0):
    print("Even Number")
else:
    print("odd Number")

# 9.Get number from the user to check primeNumber
num = int(input("Enter the number"))
count=0
for i in range(1,num+1):
    if(num%i==0):
        count+=1
if(count==2):
    print("Prime Number")
else:
    print("Not a Prime Number")

# 10. Even number change to @
num=100
for i in range (1,num+1):
    if(i%2==0):
        print("@")
    else:
        print(i)

# 11. Square of the given collection

def Square(*value):
    for i in value:
        print(i*i)
Square(1,2,3,4,5)

# 12. Dictionary
def Dictionary(**details):
    for key,value in details.items():
        print(key,":",value)
Dictionary(Name="Ahkalya",
        age=21,
        address="Chennai",
        phoneNumber=123456789)

#13.
def Userdetails():
    name = input("Enter the name : ")
    age = int(input("Enter Your Age :"))
    location = input("Enter your Location : ")
    return name,age, location

a,b,c = Userdetails()
print(f"Name:{a} age:{b} location:{c}")
#=====Looping Statements========
# 1.Write a Python program whether the given number is armstrong or not.
num=int(input("Enter a number:"))
sum=0
temp=num
while(temp>0):
    rem=temp%10
    sum=sum+rem**3
    temp=temp//10
if(sum==num):
    print("it is a armstrong number")
else:
    print("it is not a armstrong number") 

# 2.Write a python program whether the given number is palindrome or not
num=int(input("Enter a number:"))
rev=0
temp=num
while(temp>0):
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
if(rev==num):
    print("it is a palindrome number")
else:
    print("it is not a palindrome number")

# 3.Write a python program whether the given number is spy or not
num=int(input("Enter a number:"))
sum=0
prod=1
temp=num
while(temp>0):
    rem=temp%10
    sum=sum+rem
    prod=prod*rem
    temp=temp//10
if sum==prod:
    print("it is a spy number")
else:
    print("it is not a spy number")

# 4.Write a Python program Whether the given number is neon or not
num=int(input("Enter a number:"))
sum=0
sqr=num**2
while(sqr>0):
    rem=sqr%10
    sum=sum+rem
    sqr=sqr//10
if sum==num:
    print("it is a neon number")
else:
    print("it is not a neon number")

# 5.Write a python program whether the given number is harshad or not.
num=int(input("Enter a number:"))
sum=0
temp=num
while(temp>0):
    rem=temp%10
    sum=sum+rem
    temp=temp//10
if num%sum==0:
    print("it is a harshad number")
else:
    print("it is not a harshad number")

# 6.Write a Pyhon program whether the given number is perfect or not'
num=int(input("Enter a number:")) 
sum=0
i=1
while(i<=num//2):
    if(num%i==0):
        sum=sum+i
    i=i+1
if sum==num:
    print("it is a perfect number")
else:
    print("it is not a perfect number")

# Nested while 
# 7.Write a Python program whether the given number is strong or not.
num=int(input("Enter a number:"))
sum=0
temp=num
while(temp>0):
    i=1
    fact=1
    rem=temp%10
    while(i<=rem):
        fact=fact*i
        i=i+1
        sum=sum+fact
        temp=temp//10
if(sum==num):
    print("Strong number")
else:
    print("it is not strong number")

# 8.Write a Python program whether the given number is fascinating number or not.
num=int(input("Enter a number:"))
if num<100:
    print("Fasination is not defined")
else:
    result=str(num)+str(num*2)+str(num*3)
    expected_list=['1','2','3','4','5','6','7','8','9']
    if sorted(result)==expected_list:
        print("is is fasinating number")
    else:
        print("it is not a fasinating number")

# 9.Write a Python program to find factorial of given number.
num=int(input("Enter a number:"))
fact=1
if num<0:
    print("Factorial are not defined by nagative numbers")
elif num==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("Factorial of",num,"is",fact)

# 10.Write a Python program to find the is fibonacci in a given range.
a=0
b=1
value=int(input("Enter a given Range:"))
list=[0,1]
for i in range(value-2):
    result=a+b
    list.append(result)
    a=b
    b=result
print(list)

# 11.Write aPython program to find the-auto-marphic number or not.
num=int(input("Enter any number:"))
sqr=num**2
temp=sqr
if(temp>0):
    rem=temp%10
    sqr=temp//10
if num==rem:
    print("it is automorphic")
else:
    print("it is not a automorphic")

# 12.Write a Python program to find The-trio-morphic number or not.
num=int(input("Enter a number:"))
temp=num
cube=num**3
flag=0
while(cube>0):
    rem=cube%10
    if num==rem:
        flag=1
        break
    cube=cube//10
if flag==1:
    print("it is triomorphic")
else:
    print("it is not triomorphic")

# 13.Write a Python program to find the prime series in given range.
start=int(input("Enter the value:"))
end=int(input("Enter the value:"))
for i in range(start,end):
    for j in range(2,i):
        if i%j==0:
            break
        else:
            print(i,end=",")

# 14.Write a Python program to find given number is prime or not.
num=int(input("Enter a number:"))
flag=0
for i in range(2,num):
    if(num%i==0):
        flag=1
    break
if flag==1:
    print("it is not prime number")
else:
    print("it is a prime number")

#==========END OF IF, ELIF, ELSE, FOR, WHILE LOOPING STATEMENT EXAMPLES==========#


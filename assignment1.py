#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 Write a Python program which accepts the radius of a circle from the user and compute the area.
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is " + str(3.142 * r**2))


# In[2]:


#2 Python program to check if a number is positive, negative or zero :
x=int(input("enter a number : "))
if x > 0 :
    print("number is positve")
elif x < 0 :
    print("number is negative")
elif x ==0 :   
    print("number is zero")


# In[3]:


#3 Write a Python program to check whether a number is completely divisible by another number. Accept two integervalues form the user
x=int(input("enter numerator : "))
y=int(input("enter demominator : "))

z=x/y
a=x%y
print("quotient = " + str(z))
print("remainder = " + str(a))
if x%y ==0:
    print(str(x) + " is completely divisible by " + str(y))
else:
    print(str(x) + " is not completely divisible by " + str(y))


# In[4]:


#4 Write a Python program to calculate number of days between two date
f_date = date(2018, 12, 12)
l_date = date(2018, 12, 16)
delta = l_date - f_date
print(delta.days)


# In[5]:


#5 Write a Python program to get the volume of a sphere, please take the radius as input from user
r=float(input("enter the radius of sphere in cms : "))
v=(4/3)*(3.142)*r**3
print("volume of sphere is " + str(v) + " cms^3")


# In[6]:


#6 Write a Python program to get a string which is n (non-negative integer) copies of a given string
def larger_string(str, n):
   result = ""
   for i in range(n):
      result = result + str
   return result

print(larger_string('Hi', 4))


# In[7]:


#7 Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user
num = float(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")


# In[9]:


#8 Write a Python program to test whether a passed letter is a vowel or not
x=input("enter an alphabet : ").lower()
if  (x=="a" or x=="e" or x=="i" or x=="o" or x=="u") :
    print("alphabet you entered is a vowel")
else :
    print("alphabet you entered is a consonant")


# In[10]:


#9 Write a Python program that will accept the base and height of a triangle and compute the area
b = float(input("Input the base : "))
h = float(input("Input the height : "))

area = b*h/2

print("area = ", area)


# In[11]:


#10 Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years
a = int(input("Please enter principal amount: "))
b = float(input("Please Enter Rate of interest in %: "))
c = int(input("Enter number of years for investment: "))
d = 0
e = a * b * 10
while d < c:
    e += e * b
    d += 1
    
print("After",c,"years your principal amount",a,"over an interest rate of",b,"% will be",e)


# In[12]:


#11 Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
x1=int(input("enter x1 : "))
x2=int(input("enter x2 : "))
y1=int(input("enter y1 : "))
y2=int(input("enter y2 : "))
d=((x2-x1)**2 + (y2-y1)**2)**(1/2)
print("the distance between points " + str((x1,y1)) + " and " + str((x2,y2)) + " is " + str(d) + " units")


# In[13]:


#12 Write a Python program to convert height in feet to centimetres
l=float(input("enter height in feet : "))
x=l*30.48
print("height in cms is " + str(x))


# In[14]:


#13 Write a Python program to calculate body mass index
a = float(input("Enter Height in Cm: "))
b = float(input("Enter Weight in Kg: "))
c = a * 0.01
d = b / (c * c)
print("Your BMI is",d)


# In[15]:


#14 Python program to sum of the first n positive integers 
n=int(input("enter any number : "))
s=(n*(n+1))/2
print("sum of first " + str(n) + " integers is " + str(s))


# In[16]:


#15 Write a Python program to calculate the sum of the digits in an integer
num = int(input("Input a four digit numbers: "))
x  = num //1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10
print("The sum of digits in the number is", x+x1+x2+x3)


# In[17]:


#16 Write a Python program to convert an decimal integer to binary
def decimalToBinary(num):
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')
number = int(input("Enter any decimal number: "))
decimalToBinary(number)


# In[18]:


#17 Write a program to convert binary number to Decimal number
b_num = list(input("Input a binary number: "))
value = 0

for i in range(len(b_num)):
    digit = b_num.pop()
    if digit == '1':
        value = value + pow(2, i)
print("The decimal value of the number is", value)


# In[19]:


#18 Counter of Vowel and Consonents
#Answer:
str1 = input("Enter text: ")
vowels = 0
consonants = 0

for i in str1:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
       or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1

print()
print("Vowels:",vowels)
print("Consonants:",consonants)


# In[20]:


#19 Palindrome tester
my_str = input("Enter text: ")
my_str = my_str.casefold()
rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")


# In[21]:


#20 Counter of Alphabetic Numbers and Special Characters
txt = input("Enter text: ")
a = 0
b = 0
c = 0
d = 0
for x in txt:
    if int(ord(x)) >= 65 and int(ord(x)) <= 122:
        a += 1
    elif int(ord(x)) >= 48 and int(ord(x)) <= 57:
        b += 1
    elif x == " ":
        d += 1
    else:
        c += 1
print("Numbers =",b)
print("Alphabets =",a)
print("Special Characters =",c)
print("Spaces =",d)


# In[22]:


#21 Write a Python program to construct the following pattern
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# In[23]:


#22 Python program to construct following pattern
my_string = "12345"
x = 0

for i in my_string:
    x = x + 1
    print(my_string[0:x])

for i in my_string:
    x = x - 1
    print(my_string[0:x])


# In[24]:


#23 Write a Python program to construct the following pattern
for i in range(10):
    print(str(i) * i)


# In[ ]:





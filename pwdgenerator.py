import random
import string
print('Hello, Welcome to Password generator!')
length = int(input('Enter the length of password: '))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
s=random.choice(symbols)
u=random.choice(upper)
n=random.sample(num,2)
l=random.sample(lower,length-4)
temp=[]
temp.append(s)
temp.append(u)
for i in l:
    temp.append(i)
for j in n:
    temp.append(j)
random.shuffle(temp)
password = "".join(temp)
print(password)

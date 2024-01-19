import random
import string

Letters=list(string.ascii_letters)
Symbols=list(string.punctuation)
Numbers=list(string.digits)

password=[]
num_letters=int(input("how many number of letters do you want in your password"))
num_numbers=int(input("how many number of numbers do you want in your password"))
num_symbols=int(input("how many number of special characters do you want in your password"))

for i in range(1,num_letters+1):
    p=random.choice(Letters)
    password.append(p)
    
for j in range(1,num_numbers+1):
    p=random.choice(Numbers)
    password.append(p)
    
for k in range(1,num_symbols+1):
    p=random.choice(Symbols)
    password.append(p)

random.shuffle(password)
x="".join(password)
print(x)
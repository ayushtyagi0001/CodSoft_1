import string
import random

s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digits
s4=string.punctuation

passwordlen = int(input("enter the password length : "))

s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
random.shuffle(s)
print("generated passwors is : ")
print("".join(s[0:passwordlen]))


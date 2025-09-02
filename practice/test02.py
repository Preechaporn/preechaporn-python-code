"""
def i(age):
    if age>0:
        return "born"
    
a = []
a.append(i(1))
a.append(i(2))
a.append(i(3))

print(a)
"""

p = [1,2,3,4,5,]

a = max(p)
b = min(p)
c = sum(p)/len(p)
d_1 = []

for i in p:
    if i>1:
        d_1.append(i)

print(a) 
print(b)
print(c)
print(d_1)
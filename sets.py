names = {"Aryan", "Rudhvik", "Laura", "James", "Steven"}
names1 = {"Aryan", "Agatha", "Laura", "Lily", "Zack"}

names1.add("Jack")
print(names1)

print(names|names1)
print(names1|names)

print(names&names1)

print(names-names1)
print(names1-names)

print(names^names1)
print(sorted(names))

s = sorted(names)
print(sorted(names,reverse=True))

'''
var, datatypes,loops,list,tuples,dict,conditions,turtle,
datatypes conversion, matrix
pgzrun
random
string, math
'''
import string,random
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(list(string.ascii_letters))
print(random.choice(list(string.ascii_letters)))
l=[12,23,43,32,23,11]
t=(12,23,43,32,23,11)
# print(l)
# print(t)
s={12,23,43,32,23,11,11,32}
s1={78,76,56,34,11,23,32}
print(s)
print(s1)




print(s-s1)
print(s1-s)

print(s^s1)

#descending order

print(sorted(s, reverse = True))
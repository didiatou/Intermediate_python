# Liste
mylist = ["bana", "cheri", "apple"]
print(mylist)


if "apple" in mylist:
    print("yes")
else:
    print("no")

print(len(mylist))

mylist.append("lemon")
print(mylist)
rem=mylist.pop(0)
print(rem)
print( "updated list: " ,mylist)

newlist= sorted(mylist)
print(newlist) 
mylist1 = [1,2,3,4,5,6,7,8,9]
a=mylist1[::-1]
a=mylist1[::2]
print(a)


mylist_o=["bana", "cheri", "apple"]
mylistco= list(mylist_o)
mylistco.append("pinaple")
print(mylist_o)
print(mylistco)
a = [1,2,3,4,5,] 
print(a)
b= [i*i for i in a]
print(b)

#Tuple
mytuple = ("Max", 28,"Boston")
print(mytuple)
print(type(mytuple))

item = mytuple[-2]
print(item)

for x in mytuple:
    print(x)

if "Boston" in mytuple:
    print("yes")
else:
    print("no")


tuple=('e', 'e', 'd','f','r','r','r',2)
print(tuple.count('r'))
print(tuple.index('f')) 

#Dictionary
mydict = {"name": "Max", "age": 32, "city":"Paris"}
print(mydict)
mydict["mail"] =  "arri@gmail.com"
print(mydict)

if "name" in mydict:
    print("yes")
else:
    print("no")
del mydict["name"]
print(mydict)
print(mydict.popitem())

for key, value in mydict.items():
    print(key,value) 

# Sets
x = set()
x.add(1)
x.add(2)
x.add(3)
print(x)
x.discard(3)
print(x)
for i in x:
    print(i)

if 5 in x:
    print("yes")
else:
    print("no")

pds={1,3,5,7,9}
evens = {0,2,4,6,8}
primes= {2,3,5,7}
print(pds.union(evens))
print(primes.intersection(pds))
print(evens.symmetric_difference(primes))

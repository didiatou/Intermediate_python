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
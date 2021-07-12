#Method	Description
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list

mylist=[8,6,3,9,4,"bye","hello"]
mylist.append("apple")
print(mylist)
mylist.clear()
print(mylist)
mylist=[999,666,"elena","damon","stefan"]
y=mylist.copy()
print(y)
y=mylist.count("elena")
print(y)
series=["suits","TVD","PLL"]
mylist.extend(series)
print(mylist)
y=mylist.index("elena")
print(y)
mylist.insert(2,"caroline")
print(mylist)
mylist.pop(1)
print(mylist)
mylist.remove(999)
print(mylist)
mylist.reverse()
print(mylist)
mylist.sort()
print(mylist)





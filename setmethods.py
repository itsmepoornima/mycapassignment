#Method	Description
#add()	Adds an element to the set
#clear()	Removes all the elements from the set
#copy()	Returns a copy of the set
#difference()	Returns a set containing the difference between two or more sets
#difference_update()	Removes the items in this set that are also included in another, specified set
#discard()	Remove the specified item
#intersection()	Returns a set, that is the intersection of two other sets
#intersection_update()	Removes the items in this set that are not present in other, specified set(s)
#isdisjoint()	Returns whether two sets have a intersection or not
#issubset()	Returns whether another set contains this set or not
#issuperset()	Returns whether this set contains another set or not
#pop()	Removes an element from the set
#remove()	Removes the specified element
#symmetric_difference()	Returns a set with the symmetric differences of two sets
#symmetric_difference_update()	inserts the symmetric differences from this set and another
#union()	Return a set containing the union of sets
#update()	Update the set with the union of this set and others


fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
fruits.clear()
print(fruits)
food = {"biriyani", "pizza", "chicken65","cake"}
x = food.copy()
print(x)


x =  {"biriyani", "pizza", "chicken65","cake","apple"}
y = {"pizza", "microsoft", "apple",}
z = x.difference(y)
print(z)


x =  {"biriyani", "pizza", "chicken65","cake","apple"}
y = {"pizza", "microsoft", "apple",}
x.difference_update(y)
print(x)
food.discard("pizza")
print(food)



x =  {"biriyani", "pizza", "chicken65","cake","apple"}
y = {"pizza", "microsoft", "apple",}
z = x.union(y)
print(z)


z = x.intersection(y)
print(z)

x.intersection_update(y)
print(x)

z = x.isdisjoint(y)
print(z)

z = x.issubset(y)
print(z)

z = x.issuperset(y)
print(z)

z = x.symmetric_difference(y)
print(z)

x.symmetric_difference_update(y)
print(x)

x.update(y)
print(x)

food = {"biriyani", "pizza", "chicken65","cake"}
food.pop()
print(food)
food = {"biriyani", "pizza", "chicken65","cake"}
food.remove("chicken65")
print(food)



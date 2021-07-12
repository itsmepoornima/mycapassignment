#Method	Description
#clear()	Removes all the elements from the dictionary
#copy()	Returns a copy of the dictionary
#fromkeys()	Returns a dictionary with the specified keys and value
#get()	Returns the value of the specified key
#items()	Returns a list containing a tuple for each key value pair
#keys()	Returns a list containing the dictionary's keys
#pop()	Removes the element with the specified key
#popitem()	Removes the last inserted key-value pair
#setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#update()	Updates the dictionary with the specified key-value pairs
#values()	Returns a list of all the values in the dictionary

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)
car.update({"color": "White"})
print(car)
x = car.copy()
print(x)
x = car.get("model")
print(x)
x = car.items()
print(x)
x = car.keys()
print(x)
x = car.values()
print(x)
x = car.setdefault("brand")
print(x)
car.pop("model")
print(car)
car.popitem()
print(car)

car.clear()#clear
print(car)

x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

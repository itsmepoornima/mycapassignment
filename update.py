#yes we can update the value of a key in dictionary .
#by using update() function we can update the value of a key in dictionary.
thisdict = {
  "brand": "Ramraj",
  "type": "veshti",
  "colour":"white",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict)

txt = "hello, and welcome to MYWORLD."
print(txt)
x = txt.index("welcome")
print(x)
x = txt.find("welcome")
print(x)
x = txt.capitalize()
print (x)
x = txt.casefold()
print(x)
x = txt.endswith("MYWORLD.")
print(x)


txt='banana'
x = txt.center(20)
print(x)

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

txt = "My name is Ståle"
x = txt.encode()
print(x)

txt = "H\te\tl\tl\to"
x =  txt.expandtabs(5)
print(x)

txt = "For only {price:.5f} dollars!"
print(txt.format(price = 49))

txt = "Company12"
x = txt.isalpha()
print(x)
x = txt.isalnum()
print(x)
x = txt.isdecimal()
print(x)

txt = "50800"
x = txt.isdigit()
print(x)

txt = "Demo"
x = txt.isidentifier()
print(x)
x = txt.islower()
print(x)
x = txt.isnumeric()
print(x)
x = txt.isprintable()
print(x)
x = txt.isspace()
print(x)
txt = "   "
x = txt.isspace()
print(x)
txt="welcome"
x = txt.istitle()
print(x)

txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

txt = "BANANA"
x = txt.ljust(15)
print(x, "is my favorite fruit.")
x = txt.lower()
print(x)

txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)


txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")

txt = "welcome to the jungle"
x = txt.split()
print(x)

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

x = txt.title()
print(x)

x = txt.upper()
print(x)


mydict = {83:  70}#ASCII VALUE
txt = "Hello Sam!"
print(txt.translate(mydict))

txt = "50"
x = txt.zfill(10)
print(x)





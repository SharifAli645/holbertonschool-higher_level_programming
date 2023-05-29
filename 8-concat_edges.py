#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
         language that combines remarkable power with very clear syntax"
#str = str[str.find('Python'):str.find(' ',str.find('Python'))]
str = str[str.find("P"):str.find("n")+1]
print(str)

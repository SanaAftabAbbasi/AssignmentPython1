# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 11:13:19 2019

@author: Sana
"""
#First Builtin Function
frnd1 = input("Enter First Friend Name:   ")
frnd2 = input("Enter Second Friend Name:   ")
frnd3 = input("Enter Third Friend Name:   ")
frnd4 = input("Enter Fourth Friend Name:   ")
frnd5 = input("Enter Fifth Friend Name:   ")
Friends = [frnd1,frnd2,frnd3]
#Second Input Function
Friends.insert(1,frnd4)
#Third Built in Function
Friends.append(frnd5)
#Fourth Builtin Function
print("Your Friends Are")
for i in Friends:
    print(i,end=" , ")
#Fifth BuiltIn Function
print(Friends.count("Sana"))
#Sixth BuiltIn Function
print(Friends.index("Sana"))
#Seventh BuiltIn Function
Friends.clear()

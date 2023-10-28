"""Dictionaries practice"""

ice_cream: dict[str,int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

#add new element
#do not use append
#<dict name>[key] = <value>

ice_cream["mint"] = 3

#when using f string, no double quotation inside the f string
#e.g. chocolate should be ''

ice_cream["vanilla"] = 10
len(ice_cream) #how many key-value pairs you have

#check if key in dictionary
#<key> in <dict name>
if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("no orders of mint")

#important note: dictionary can't have multiple same keys
#but can have multiple identical values

#for loop
for key in ice_cream:
    print(key)
for key in ice_cream:
    print(f"{key} has {ice_cream[key]} orders.")

monthConversions = {
    "January" : "Janvier",
    "February" : "Fevrier",
    "March" : "Mars",
    "April" : "Avril",
    "May" : "Mai", 
    "June" : "Juin",
    "July" : "Juillet",
    "August" : "Aout",
    "September" : "Septembre",         # Key : Value
    "October" : "Octobre",
    "November" : "Novembre",
    "December" : "Decembre",
    1 : "Un",
    2 : "Deux",
    3 : "Trois"
}

print(monthConversions["August"])
print(monthConversions.get("March"))
print(monthConversions[2])
#print(monthConversions["Banana"]) #using a non-existing key to access a value throws an error.
print(monthConversions.get("Banana")) #using the get() function returns None when we input a non existing key
print(monthConversions.get("Banana", "Not Found"))
print(monthConversions.get("March", "Default argument for when the key doesn't exist"))

monthConversions["alpha"] = "aleph" #adding new key-value pair to our dictionary
print(monthConversions["alpha"])

print(monthConversions)

# This is how to update multiple key value pairs simultaneously:
monthConversions.update({"alpha" : "beta", 1 : "Uno", 2 : "Dos", 3 : "Tres"}) 

print(monthConversions)
monthConversions[3] = "Drei" #Changing key-value pairs one at a time
print(monthConversions[3])

#del monthConversions['alpha']
#print(monthConversions.get('alpha'))

alpha = monthConversions.pop('alpha') #Pop method removes and 
print(alpha)  #also returns a value, so it allows us to grab the removed value with a variable
#creating dictionary using "{ }"

dict = { 
    "first name" : "prathamesh",
    "last name" : "wadkar"
}
print(dict['first name'])

#it is an un-ordered list
#so we can not access elements using index
#print(dict[1]) #dives error

# we can insert list into dictionary
dict = { 
    "first name" : "prathamesh",
    "last name" : "wadkar",
    "phone no" : [98504 , 94048, 98233]
}
print(dict['phone no'])
#we can modify the list
dict['phone no']= [99600, 94230]
#entire list get updated
print(dict['phone no'])

#we can create nested dictionary
dict = { 
    "first name" : "prathamesh",
    "last name" : "wadkar",
    "phone no" : { "telephone" : '02312xyz'}
}
print(dict['phone no'])
print(dict['phone no']['telephone'])

#methos related to dictionaries
dict = { 
    "firstname" : "prathamesh",
    "lastname" : "wadkar",
    "phoneno" : { "telephone" : '02312xyz'},
    1: 1000,
    5: 5000
}

#to get keys present in the dictonary
print(dict.keys())

# to get values
print(dict.values())

#to get all content
print(dict.items())  

#updating the dictionary
updt = {
    
    "address" : 795,
    "city": "kolhapur"
}
dict.update(updt)
print(dict)

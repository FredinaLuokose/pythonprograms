dictionary = {}
dictionary = {'Name': 'Tanu', 'Sex': 'Male', 'Age': 23}
print(dictionary)
dictionary.update({"color":"red"}) #add elements
print(dictionary)
print(dictionary['Sex']) #accesing the elements
del dictionary['Name']
print(dictionary)#deleting the elements
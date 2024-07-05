person={"name":"fredu","age":"24","home":"pkd"}
print(person["name"])
print(person["age"])
print(person["home"])
person.update({"color":"red"})
print(person)
del person["name"]
print(person)
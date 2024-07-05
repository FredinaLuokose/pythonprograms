def group(list,size):
    for i in range(0,len(list),size):
        return list[i:i+size]

list=[1,2,3,66,4,7]
size=2
g=group(list,size)
print('group=',g)
def swap(list,pos1,pos2):
    temp=list[pos1]
    list[pos1]=list[pos2]
    list[pos2]=temp
    return list
list=[23,65,19,90]
pos1,pos2= 1,3
print(swap(list, pos1-1, pos2-1))
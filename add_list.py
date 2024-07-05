def add_lists(list1,list2):
    min_length=min(len(list1),len(list2)) 
    result=[list1[i]+list2[i] for i in range(min_length)]
    if len(list1)>len(list2):
        result.extend(list1[min_length:])
    elif len(list2)>len(list1):
                result.extend(list2[min_length:])
    return result
list1=[1,2,3,4]
list2=[5,6,7]
result=add_lists(list1,list2)
print(result)
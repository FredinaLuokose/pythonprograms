
def unique_dup(un):
    u,du=[],[]
    print("original list:",un)
    for i in un:
        if i not in u:
            u.append(i)
        
        else: 
            du.append(i)
    print("unique",u,"\n dupe:",du)
unique_dup([1,2,3,2,1,3,4])

def dup(dl):
    dup_list = []
    or_list =[]
    for i in dl:
        if i not in or_list:

            or_list.append(i)
        else:
            dup_list.append(i)
    print('dup=',dup_list)
ul2=[1,2,3,3,5,5]
dup(ul2)

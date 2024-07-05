def search_string(str,file):
    f=open(file).readlines()
    for line in f:
        if str in line:
            print(f'exist {str} in {file}')
        else:
            pass

str1='amzsys'
file1 = 'hello.c'
search_string(str1,file1)
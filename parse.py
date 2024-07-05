def parse_csv(filename):
    new_file=[]
    f=open(filename).readlines()
    for line in f:
        nl=line.split()
        new_file.append(nl)
    return new_file
file1='file.csv'
print(parse_csv(file1))

print('..dictionarys....')
a={'name':'milu','email':'milu@gmail.com'}
print(a.keys())
print(a.values())
print(a.items())
print(a['name'])

if 'name' in a:
    print('true')
k=a.get('email')
if k is not None:
    print('exist')
add=a.setdefault('age','24')
print(a)
t='hello %(name)s' % {'name': 'python'}
print(t)
t1='welcome %(name)s' % {'name':'Amzsys'}
print(t1)
print('word count')
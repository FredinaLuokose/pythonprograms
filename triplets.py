n=25
new3 = [(x,y,z) for x in range(1,n) for y in range(x,n) for z in range(y,n) if x*x + y*y == z*z]
print(new3)
for index,value in  enumerate(['a','b','c']):
    print(index,value)
print('p-29')
def d_array(r,c):
    return [[None for i in range(c)] for j in range(r)]
r=2
c=3
a=d_array(r,c)
for row in a:
    print(row)

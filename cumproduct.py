
def cumulative_product(cl):
    cum_sum = []
    sum=1
    for i in cl:
        sum=sum*i
        cum_sum.append(sum)
    return cum_sum
cl=[1,2,3,4,5]
print('original list=',cl)
print('cumulative product=',cumulative_product(cl))
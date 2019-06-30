def lx_sum(my_dict):
    sum=0
    for k,v in my_dict.items():
        sum=sum+v
    return sum

def lx_len(my_dict):
    sum=0
    for k,v in my_dict.items():
        sum=sum+1
    return sum

d = {'piggy': 23, 'sheepy': 30, 'tiger': 45,'chicken':50}
n=lx_len(d)
a=lx_sum(d)/n
s='average:%s' %(a)
print(s) 

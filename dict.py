d = {'piggy': 23, 'sheepy': 30, 'tiger': 45,'chicken':50}
n=len(d)
sum=0
for k,v in d.items():
    sum=sum+v
a=sum/n
s='average:%s' %(a)
print(s)
    
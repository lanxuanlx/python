animals=['piggy','sheepy','cow','tiger']
for animal in animals:
    print(animal)

sum=0
for x in range(101):
    sum=sum+x
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('hello,%s'%name)

n = 0
while 'piggy':
    n=n+1
    if n%2 != 0:
        continue 
    print(n)
    if n > 10000:
        break
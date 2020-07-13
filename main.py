import random
l1 = random.sample(range(1,100), 10)
print(l1)
l2 = random.sample(range(1,100), 20)
print(l2)

#res = [i for i in l1 and i in l2]
res = []
for i in l1:
  if i in l2:
    res.append(i)
print(f'common elements: {res}')

res = [i for i in l1 if i in l2]
print(f'common elements (using list comp): {res}' )
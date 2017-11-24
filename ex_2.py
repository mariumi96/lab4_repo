from librip.gens import gen_random
from librip.iterators import Unique
data = [1,1,1,2,2,2,2,2]
my_order = Unique(data)
for i in my_order:
    print(i, end = ' ')
print()

data2 = gen_random(1,3,10)
my_order = Unique(data2)
for i in my_order:
    print(i, end = ' ')
print()

data3 = ['a','A','b','B','a']
my_order = Unique(data3) # ignore_case = False
for i in my_order:
    print(i, end = ' ')
print()

data4 = ['a','A','b','B']
my_order = Unique(data4, True) # ignore_case = True
for i in my_order:
    print(i, end = ' ')
print()
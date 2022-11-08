"""t_1 = round(((3 - 1)**2 + (2-1)**2)**(1/2), 2)
t_2 = round(((5 - 3)**2 + (5-2)**2)**(1/2), 2)
t_3 = round(((6 - 5)**2 + (6-5)**2)**(1/2), 2)
t_4 = round(((10 - 6)**2 + (8-6)**2)**(1/2), 2)
print(t_1 + t_2 + t_3 + t_4)

def average(a, b):
    return (a + b)/2
a = int(input())
b = int(input())
print(average(a, b))

def regestration(name, course = 'Introduction in the programming', time = '6 semester'):
    print('Dear,', name)
    print('You have regestration on course:', course, 'for', time)
regestration('Andrew')
regestration('Andrew', 'abugagaga', '1000000 years')

def average(*numbers):
    summ_s = sum(numbers)
    l = len(numbers)
    return summ_s/l

import calculation
print(calculation.average(1,2))
print(calculation.maximum(16, 80))

import calculation as avg
import math
print(avg.average(1, 2))
print(pope.pi)

from  matplotlib import pyplot as plt
x = [-3, -2, -1, 0, 1, 2, 3]
y = [9, 4, 1, 0, 1, 4, 9]
print(plt.plot(x, y))
"""
import math
z = list(range(-7, 74, 2))

y = []
i = 0
p = 0
while i <= len(z)-1:
    y.append(z[p])
    i += 1
    p += 1
print(y)







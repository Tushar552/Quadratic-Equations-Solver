print('------------------------------SOLVE QUADRATIC EQUATION---------------------------------')
a = input('a = ')
b = input('b = ')
c = input('c = ')
print('--------------------------------------------------------------------------')
print('   ')
print('quadratic equaton = ax^2 + bx + c = (',a,')x^2 + (',b,')x + (',c,')')
print('    ')
import math
d = int(b)**2 - 4*int(a)*int(c)
print('discrimant = b^2 - 4ac =',d)
if d >= 0:
    print('------------------------------from quadratic formula we get----------------------------')
    print('           ')
    e = int(b) * -1
    f = int(e) + math.sqrt(int(d))
    g = int(a) * 2
    h = int(e) - math.sqrt(int(d))
    i = int(f) / int(g)
    j = int(h) / int(g)
    print('zeros of quadratic polynomial = -(b) +- sqrt(d)/2a = ', i, 'or', j)
    print('            ')
    print('---------------------------------------------------------------------------------------')
    print('-----------------------------from factorisation method---------------------------------')
    print('           ')
    print('=> ax^2 + bx + c = (', a, ')x^2 + (', b, ')x + (', c,')= 0')
    print('=> { x + (',i,')} { x + (',j,')}')
    print('=> x =',i,' or x =',j)
    print('            ')
    print('-------------------------------------- solved --------------------------------------')
else:
    print("Can't solve . Discrimant is negative !")



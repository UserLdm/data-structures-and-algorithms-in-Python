#如果a+b+c=1000,且a^2+b^2=c^2(a,b,c为自然数),如何求出a,b,c可可能的组合
#枚举法

import time

#start_time = time.time()
#for a in range(0, 1001):
#    for b in range(0, 1001):
#        c = 1000 - a - b
#        if a**2 + b**2 == c**2:
#            print("a,b,c:%d,%d,%d"%(a, b, c))
#end_time = time.time()
#print("times:%d"%(end_time - start_time))


start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001-a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a,b,c:%d,%d,%d"%(a, b, c))
end_time = time.time()
print("times:%f"%(end_time - start_time))





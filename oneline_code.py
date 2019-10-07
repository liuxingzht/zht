#一行代码实现1-100求和
print(sum([i for i in range(1,101)]))
#一行代码实现1-100奇数
[print(i, end=' ') for i in range(101) if i % 2 != 0] 
#一行代码实现1-100偶数
[print(i, end=' ') for i in range(101) if i % 2 == 0]
#一行代码实现九九口诀表
print('\n'.join([' '.join(["%2s x%2s = %2s"%(j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))
#一行代码打印迷宫
print(''.join(__import__('random').choice('\u2571\u2572') for i in range(50*24)))
#一行代码心形Love
print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))
#一行代码水仙花数（方法一)
print(list(map(lambda x: x[1], filter(lambda x: x[0], [(i*100+j*10+k == i**3+j**3+k**3, i**3+j**3+k**3) for i in range(1, 10) for j in range(0, 10) for k in range(0, 10)]))))
#一行代码水仙花数（方法二)
print([i**3+j**3+k**3 for i in range(1, 10) for j in range(0, 10) for k in range(0, 10) if i*100+j*10+k == i**3+j**3+k**3])
#一行代码实现三个数子的回文数
print([i*100 + n*10 + m for i in range(1,10) for n in range(10) for m in range(1,10) if i == m])
#一行代码解决1-100，3的倍数，5的倍数，3and5的倍数
print(' '.join(["fizz"[x % 3 * 4:]+"buzz"[x % 5 * 4:] or str(x) for x in range(1, 101)]))
#一行代码输出斐波那契数列
print([x[0] for x in [(a[i][0], a.append([a[i][1], a[i][0]+a[i][1]])) for a in ([[1, 1]], ) for i in range(30)]])

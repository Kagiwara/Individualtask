n, W = input().split()
W = int(W)
items = []
total_c = 0
for i in range(int(n)):
    c, m = input().split()
    items.append([float(c),int(m),float(c)/int(m)])
items.sort(reverse = True, key = lambda x: x[2])
for k in range (len(items)):
    if W == 0:
        break
    elif items[k][1] <= W:
        total_c += items[k][0]
        W -= items[k][1]
    else:
        total_c += W*items[k][2]
        break
print('%.3f' % total_c)
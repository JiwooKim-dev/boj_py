n = int(input())

for i in range(n):
    for j in range(1, n+1):
        if j % 2 == 1:
            print('* ', end='')
    print('')
    for j in range(1, n+1):
        if j % 2 == 0:
            print(' *', end='')
    print('')
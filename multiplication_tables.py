'''
Program multiplication tables from 2 to 7
'''

for i in range(1, 11):
    for j in range(2, 7):
        print('{:2} *{:2} = {:2}  '.format(j, i, j*i), end='')
    print()
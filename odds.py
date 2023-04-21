
'''
5 friends are going to play a race
It shows all the possible results that can be given in that race.
'''

friends = ['Tomas', 'María', 'Laura', 'Miguel', 'Carlos']
count = 0

for i in friends:
    for j in friends:
        for k in friends:
            for m in friends:
                for n in friends:
                    if i != j and i != k and i != m and i  != n and \
                        j != k and  j != m and j != n and \
                        k != m and k != n and \
                        m != n:
                        order = [i, j, k, m, n]
                        count += 1
                        print('{:3d} : {}'.format(count, order))


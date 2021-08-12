

n = int(raw_input())

#for i in range(1,n):
#	for j in range(1,n)

#print(len(n))

#print n%10

#print n/10

possibilities = [[0],[1]]

for i in range(0,n-1):
        l = len(possibilities)
        for p in range(0,l):
                po = possibilities[p]
                ne = []
                for pe in po:
			ne.append(pe)	
                ne.append(0)
                possibilities.append(ne)
		po.append(1)

for p in possibilities:
	print p

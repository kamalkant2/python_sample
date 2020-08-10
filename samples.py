# get the non-uniques , non duplicate number from two list without using set method:
# 
l1 = ['abc', 'xyz', 'pqr']
l2 = ['cde', 'xyz', 'pqr', 'mno']
l3 = l1+l2
result = []
k = 0
for i in range(len(l3)):
    k = k+1
    for j in range(k, len(l3)):
        print (i, l3[i], j, l3[j])
        if l3[i]  != l3[j]: # change to equal to get common between two list
            if l3[i] not in result:
                result.append(l3[i])
            if l3[j] not in result:
                result.append(l3[j])
                
print (result)

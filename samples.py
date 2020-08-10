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

# find the smallest number in python list without using sort or min function
# 2. sub problem :- sorting required ? Not exactly.
# 3. sub problem :- min required, yes for sorting and the given problem

## below is the function to get the smallest number
my_list = [-15, -26, 15, 1, 23, -64, 23, 76]
def smallest(l):
    mySmall = l[0]
    for num in l:
        if mySmall > num:
            mySmall = num
    return mySmall


result_sorted = []
for i in range(len(my_list)):
    smaller = smallest (my_list)
    result_sorted.append(smaller)
    my_list.remove(smaller)

print (result_sorted)

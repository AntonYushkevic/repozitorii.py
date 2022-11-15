list_to_sort = [[1,2,5], [2,3,3], [0,0,0], [7,9,1], [1,1,7], [1,1,1], [3,3,3]]

resl = sorted(list_to_sort, key = lambda x: x[2])

res2 = (map(lambda x: x[0]+x[1]+x[2], list_to_sort))

res3 =list(filter(lambda x: x[0]==x[1] and x[1]==x[2], list_to_sort))


print(resl)
print(res2)
print(res3)





numbers_list = [1,2,3,4,5,6,7]

new1 = [1**2 for i in numbers_list]
print(new1)




new2 = [i for i in numbers_list if i %2==1] 
print(new2)

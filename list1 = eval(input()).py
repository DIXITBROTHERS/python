list1 = eval(input())
n = int(input())
list2= []
for i in range(-1,-n-1,-1):
    list2.append(list1[i])
for ele in list2:
    list1.remove(ele)
# print(list1)
list2 = list2[::-1]
for ele in list1:
    list2.append(ele)
print(list2)

    
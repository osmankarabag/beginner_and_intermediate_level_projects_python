list1 = [1,2,3]
list2 = [1,2,3,4]
list3 = list2.copy()
list4 = list1
tot_list = [list3] + [list4]
new_list = list1 + list4
list2.pop()
list4.append(4)
print(list2 is list3)
print(list2 == list3)
print(list4 is list3)
print(list1 == list4)
list1.append(8)
print(tot_list)
print(len(set(new_list)))

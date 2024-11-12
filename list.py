
#creating an empty list
my_list=[]
#appending elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Inserting the value 15 at the second position in the list.
my_list.insert(1, 15)

#Extending my_list with another list
my_list.extend([50, 60, 70])

#Removing the last element from my_list
del my_list[-1]

#Sorting my_list in ascending order.
my_list.sort()

#Finding and printing the index of the value 30 in my_list
index_of_thirty = my_list.index(30)

print(index_of_thirty)
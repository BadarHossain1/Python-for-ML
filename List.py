my_list = [1,"Two",3,4,5]
print(my_list)  
type(my_list)

# [1, 'Two', 3, 4, 5]


#Lists are Mutable

my_list[2] = "Three"
print(my_list)
my_list.append(6)
print(my_list)

# [1, 'Two', 'Three', 4, 5]
# [1, 'Two', 'Three', 4, 5, 6]

del my_list[4]
print(my_list)

# [1, 'Two', 'Three', 4, 6]

list_2 = [2,5,3,6,7]
list_3 = list_2 + my_list
print(list_3)

# [2, 5, 3, 6, 7, 1, 'Two', 'Three', 4, 6]

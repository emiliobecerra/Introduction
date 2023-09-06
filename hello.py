# print("Hello 2 again!")

# a = 1
# b = 2

# c = a + b

# d = "Hello Hello!"

# print(d)

num_list = [1, 2, 3, 4]

# for num in num_list:
# 	print(num)

# print(num_list[0])
# print(num_list[1])
# print(num_list[2])
# print(num_list[3])
# print(num_list[4])

# name_list = ["John", "Mary", "Tom"]

# # for loop
# for name in name_list:
# 	for num in num_list:
# 		print(name + str(num))

# name_list = ["John", "Mary", "Tom"]

# # Saving values into an empty list
# another_list = []
# for num in num_list:
# 	another_list.append((num + 3)*2)
# print(another_list)

# #Alternative Way and a little bit faster without having to create an empty list
# another_list2 = [(num + 3)*2 for num in num_list]
# print(another_list2)

# #Conditional Statement
# for num in another_list:
# 	if num > 11:
# 		print(num)

# for num in another_list:
# 	if (num > 11):
# 		print("Big Number: " + str(num))
# 	else:
# 		print("Small Number: " + str(num))

# for num in another_list:
# 	if (num > 11):
# 		print("Big Number: " + str(num))
# 	elif (num < 9):
# 		print("Small Number: " + str(num))


def my_function():
	print("Hello World!")
	

	my_function()

	def augmented_numbers(num1, num2):
		return (num1 + num2) ** 2

	print(augmented_numbers(1, 2) + 2)

print(augmented_numbers(
	(augmented_numbers(1, 2) +2),
		augmented_numbers(2, 3)
	)
)










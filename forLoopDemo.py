numbers_list = [2, 4, 6, 8, 10, 11]

for numbers in numbers_list:  # Iterate over each number in the list
    if numbers % 2 == 0:
        print(f"{numbers} is even")
    else:
        print(f"{numbers} is not divisible by 2")

        
# def are_numbers_even(list) :
#     for numbers in list:  # Iterate over each number in the list
#         if numbers % 2 == 0:
#             print(f"{numbers} is even")
#         else:
#             print(f"{numbers} is not divisible by 2")

# numbers_list = [2, 4, 6, 8, 10, 11]
# second_numbers_list = [1, 2, 5, 6]
# third_numbers_list = [3, 4, 7, 8]
# are_numbers_even(numbers_list)
# are_numbers_even(second_numbers_list)
# are_numbers_even(third_numbers_list)
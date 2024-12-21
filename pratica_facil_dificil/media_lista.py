numbers_list = [10, 20, 30, 40, 50]
sum_numbers = 0
for number in numbers_list:
    sum_numbers += number

average_numbers = sum_numbers / len(numbers_list)
print(f"Average: {average_numbers:.2f}")

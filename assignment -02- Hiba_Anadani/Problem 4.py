def get_even_numbers(input_list):
    even_numbers = []
    i = 0

    while i < len(input_list):
        number = input_list[i]
        if number % 2 == 0:
            even_numbers.append(number)
        i += 1

    return even_numbers

user_input = input("Input: ")
user_list = [int(num) for num in user_input.split(",")]
print("Output:", get_even_numbers(user_list))

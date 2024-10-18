# def sum_tuples(tup1, tup2):
#     result = []
#     for i in range(len(tup1)):
#         result.append(tup1[i] + tup2[i])
#     return tuple(result)
#
# def dict_to_json_file(dictionary, filename):
#     # Start the JSON content string
#     json_content = '{\n'
#     # Loop through dictionary items
#     for key, value in dictionary.items():
#         # Add each key-value pair to the JSON content
#         json_content += f'  "{key}": "{value}",\n'
#     # Remove the last comma and close the JSON string
#     json_content = json_content.rstrip(',\n') + '\n}'
#     # Write the JSON content to a file
#     with open(filename, 'w', encoding='utf-8') as file:
#         file.write(json_content)
#
# def json_file_to_dicts(filename):
#     # Open the file and read its content
#     with open(filename, 'r', encoding='utf-8') as file:
#         content = file.read().strip()
#     # Remove the outer braces and split the content into items
#     content = content[1:-1].strip().split(',')
#     # Create an empty dictionary to store the items
#     dictionary = {}
#     # Loop through the items and add them to the dictionary
#     for item in content:
#         key, value = item.split(':')
#         key = key.strip().strip('"')
#         value = value.strip().strip('"')
#         dictionary[key] = value
#     # Return the dictionary inside a list
#     return [dictionary]
#
# def display_menu():
#     print("1. Sum Tuples")
#     print("2. Export JSON")
#     print("3. Import JSON")
#     print("4. Exit")
#
# while True:
#
#     display_menu()
#     choice = input("Enter a choice: ")
#
#     if choice == '1':
#         tup1 = tuple(map(int, input("Enter the first tuple (e.g., 1 2 3): ").split()))
#         tup2 = tuple(map(int, input("Enter the second tuple (e.g., 4 5 6): ").split()))
#         result = sum_tuples(tup1, tup2)
#         print("The result is:", result)
#     elif choice == '2':
#         # Get the dictionary from the user
#         dictionary = input("Enter a dictionary in key:value format (e.g., name:Alice age:30): ")
#         dict_items = dictionary.split()
#         dict_parsed = {item.split(':')[0]: item.split(':')[1] for item in dict_items}
#         # Get the filename from the user
#         filename = input("Enter the filename to save the JSON: ")
#         # Save the dictionary to a JSON file
#         dict_to_json_file(dict_parsed, filename)
#         print(f"Dictionary saved to {filename}")
#     elif choice == '3':
#         # Get the filename from the user
#         filename = input("Enter the JSON filename to import: ")
#         # Import the JSON content and print the dictionaries
#         dictionaries = json_file_to_dicts(filename)
#         print("Dictionaries imported:", dictionaries)
#     elif choice == '4':
#         print("Exiting the program.")
#         break
#     else:
#         print("Invalid choice, please try again.")

# problem 2
# a. O(N3) b. O(N3) c. O(N!) d. O(NlogN) e. O(N) f. O(N2) g. O(N2) h. O(N!)
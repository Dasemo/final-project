import random

def ask_number():
  
    num = int(input("Enter a number between 1 and 10: "))
    while 10 < num < 1:
        num = int(input("Please enter a valid number between 1 and 10: "))
    return num

def generate_list(length):
    list = []
    for i in range(length):
        list.append(random.randint(1, 100))
    return list

def find_min(lst):
  return min(lst)

num = ask_number()
lst = generate_list(num)
print(f"The random list generated is {lst}")

minimum = find_min(lst)
print(f"The minimum of the list is: {minimum}")

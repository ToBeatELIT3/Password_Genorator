import random

char_list = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z"
]

num_list = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9
]

spec_list =[
    "!",
    "@",
    "#",
    "$",
    "%",
    "+",
    "-",
    "*",
    "/"
]

def generate_password(number_of_chars, number_of_nums, number_of_spec):
    output_list = []
    final_list = []

    for x in range(int(number_of_chars)): output_list.append(random.choice(char_list))
    for x in range(int(number_of_nums)): output_list.append(random.choice(num_list))
    for x in range(int(number_of_spec)): output_list.append(random.choice(spec_list))
    for x in range(len(output_list)): final_list.append(str(output_list[x]))

    final_password = "".join(random.sample(final_list, len(final_list)))
    
    print(final_password)

def main():
    letter_amount = input("Enter Desired Number of Letters : ")
    number_amount = input("Enter Desired Number of Integers : ")
    special_amount = input("Enter Desired Number of Special Charecters : ")

    try: generate_password(letter_amount, number_amount, special_amount)
    except: print("\n[ERROR] Check Your Inputs Again")

if __name__ == "__main__": main()

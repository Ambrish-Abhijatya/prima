user_input = input("Enter some text:\n")
lower_count = 0
upper_count = 0
whitespace_count = 0
num_count = 0
spl_char_count = 0
for letter in user_input:
    if letter == " ":
        whitespace_count += 1
    elif letter.islower():
        lower_count += 1
    elif letter.isupper():
        upper_count += 1
    elif letter.isdigit():
        num_count += 1
    else:
        spl_char_count += 1

print(f'The number of whitespaces in your entered text is {whitespace_count}')
print(f'The number of uppercase letters in your entered text is {upper_count}')
print(f'The number of lowercase letters in your entered text is {lower_count}')
print(f'The number of digits in your entered text is {num_count}')
print(f'The number of special characters in your entered text is {spl_char_count}')




an_letters = "aefhilmnorsAEFHILMNORS"
word = input("I will cheer for you. Enter a word: ")
times = int(input("Enthusiasm Level(1 - 10): "))

i=0
for char in word:
    if char in an_letters:
        print("Give me an {}!".format(char))
    else:
        print("Give me a {}!".format(char))

print("What does that spell?")
for j in range(times):
    print(word.upper(), "!!!")

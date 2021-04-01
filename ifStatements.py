is_Male = 0
is_Tall = 1

if is_Male and is_Tall:
    print("You are a tall male.")

elif is_Male and not(is_Tall):
    print("You\'re a short male.")

elif not(is_Male) and is_Tall:
    print("You\'re a tall female.")
else:
    print("You\'re a short female.")

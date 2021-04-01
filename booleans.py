def can_run_for_president(age):
    return age >= 35
print(
    "Can a 19 year old run for president?", can_run_for_president(19),
    "\nCan a 45 year old run for president?", can_run_for_president(45)
)

def is_odd(x):
    return x%2 == 1

print("Is 205 odd?", is_odd(205))
print("Is 300 odd?", is_odd(300))

print(-6%4 == 2)

def inspect(x):
    if x > 0:
        print(x, " is positive.")
    elif x < 0:
        print(x, " is negative.")
    elif x == 0:
        print(x, " is zero.")
    else:
        print(f"{x} is unlike anything I've ever seen...")

inspect(0)
inspect(-1)
inspect(15)

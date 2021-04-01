import random

feet_to_miles = 5280
meters_to_kilometeres = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]


def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)
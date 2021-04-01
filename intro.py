#from my_modules import find_index, test
#import sys
import random
courses = ['History', 'Math', 'Physics', 'CompSci']

'''index = find_index(courses, 'Math')
#print(index)
#print(test)
#print(sys.path)'''

random_course = random.choice(courses)
print(random_course)

import math
print( round(math.sin(math.pi)))
rads = math.radians(180)
print(f'The cosine of 180 degrees is {math.cos(rads)}.' )

import datetime
import calendar

today = datetime.date.today()
print( 'Today is: ', today)
print('Is 2021 a leap year? - ',calendar.isleap(2021))
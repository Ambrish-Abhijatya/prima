courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses.index('Physics'))
print('Art' in courses)
print('Math' in courses)
course_str = ', '.join(courses)
print('This is the list separated by commas:' ,course_str)
new_list = course_str.split(', ')
print('And here\'s that string split into a list again:' ,new_list)
'''for subject in courses:
    print(subject)'''

for index, subject in enumerate(courses, start=1): #start is 0 by default when the 2nd argument is omitted
    print(index, subject)

nums = [1, 5, 2, 4, 3]
#nums.sort() #The sort method modifies the original list
sorted_nums = sorted(nums) #while the sorted function doesn't
print(nums)
print(sorted_nums)
print(min(nums))
print(max(nums))
print(sum(nums))